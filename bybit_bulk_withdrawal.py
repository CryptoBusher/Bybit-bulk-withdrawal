"""
Script for withdrawing assets from Bybit account
Bybit API docs: https://bybit-exchange.github.io/docs/v5/intro
"""

import json
from sys import stderr, exit
from random import randint, uniform, shuffle
from time import sleep
from datetime import datetime

from pybit.unified_trading import HTTP
from loguru import logger
from pyfiglet import Figlet

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>")

f = Figlet(font='5lineoblique')
print(f.renderText('Busher'))
print('Telegram channel: @CryptoKiddiesClub', 'Telegram chat: @CryptoKiddiesChat', 'Twitter: @CryptoBusher',
      sep='\n', end='\n\n')


class WithdrawException(Exception):
    pass


def withdraw(session: HTTP, coin: str, chain: str, address: str, amount: str):
    try:
        return session.withdraw(
            coin=coin,
            chain=chain,
            address=address,
            amount=amount,
            timestamp=int(datetime.now().timestamp() * 1000)
        )
    except Exception as e:
        raise WithdrawException(e)


def start_batch_withdrawal(_config: dict, _wallet_addresses: list):
    session = HTTP(
        api_key=_config["bybit_api_key"],
        api_secret=_config["bybit_api_sign"],
        testnet=False,
    )

    for i, wallet in enumerate(_wallet_addresses):
        amount_digits = randint(_config["random_min_amount_digits"], _config["random_max_amount_digits"])
        amount = str(round(uniform(_config["withdraw_min_amount"], _config["withdraw_max_amount"]), amount_digits))

        logger.info(f'{wallet} - sending {amount} {_config["withdraw_coin_ticker"]}')
        try:
            result = withdraw(
                session,
                _config["withdraw_coin_ticker"],
                _config["withdraw_network"],
                wallet,
                amount
            )

            if result["retMsg"] == 'success':
                logger.info(f'{wallet} - sent tokens, id: {result["result"]["id"]}')
            else:
                logger.error(f'{wallet} - failed to send tokens, response: {result}')

        except WithdrawException as e:
            logger.error(f'{wallet} - failed to send tokens, reason: {e}')

        if i < len(_wallet_addresses) - 1:
            delay = randint(_config["withdraw_min_delay_sec"], _config["withdraw_max_delay_sec"])
            logger.info(f'Sleeping {round(delay / 60, 2)} minutes')
            sleep(delay)


if __name__ == "__main__":
    with open('data/config.json', 'r') as f:
        config = json.loads(f.read())
    with open(f'data/wallet_addresses.txt') as file:
        wallet_addresses = [line.strip() for line in file]

    if config["shuffle_wallet_addresses"]:
        shuffle(wallet_addresses)

    confirm_action = input(f'Going to withdraw {config["withdraw_min_amount"]} - {config["withdraw_max_amount"]} '
                           f'{config["withdraw_coin_ticker"]} in {config["withdraw_network"]} network (random digits '
                           f'{config["random_min_amount_digits"]} - {config["random_max_amount_digits"]}) to '
                           f'{len(wallet_addresses)} different wallets with delay {config["withdraw_min_delay_sec"]} - '
                           f'{config["withdraw_max_delay_sec"]} seconds\n'
                           f'Are you sure? (y/n): ')

    if confirm_action.lower() == 'n':
        logger.info('User cancelled operation, quitting')
        exit()
    elif confirm_action.lower() == 'y':
        logger.info('User confirmed operation, starting')
        start_batch_withdrawal(config, wallet_addresses)
        logger.info('Finished batch withdrawal')
    else:
        logger.error('Wrong entry, quitting')
        exit()
