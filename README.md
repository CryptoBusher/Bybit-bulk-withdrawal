## Скрипт для вывода монет с биржи Bybit
Скрипт предназначен для вывода крипты с биржи Bybit с учетом рандомизации. Будет полезно дропхантерам, так как на данной бирже низкие комиссии на выводы в сети ERC-20. 

Связь с создателем: https://t.me/CrytoBusher <br>
Залетай сюда, чтоб не пропускать дропы подобных скриптов: https://t.me/CryptoKiddiesClub <br>
И сюда, чтоб общаться с крутыми ребятами: https://t.me/CryptoKiddiesChat <br>

## Первый запуск
1. Устанавливаем Python 3.10.
2. Качаем репозиторий.
3. Открываем терминал, переходим в папку с файлами и пишем команду "pip install -r requirements.txt".
4. Открываем файл "data/wallet_addresses.txt" и вставляем свои кошельки, на которые будем получать монеты (каждый кошелек с новой строки).
5. Создаем API ключ на бирже Bybit (system-generated API keys). Даем ключу Read-Write permissions, указываем свой IP адрес, даем право на Withdrawal.
6. Добавляем свои кошельки в Whitelist на бирже Bybit (Account and security -> Withdrawal security -> Withdrawal address whitelist). Без этого нельзя производить выводы через API. Можно накидать скрипт в Zennoposter или на BAS, чтоб не делать это руками.
7. Открываем файл "data/config.json" и забиваем настройки:
   - _**bybit_api_key**_ - API ключ, получаемый в разделе API на бирже Bybit
   - _**bybit_api_sign**_ - ключ, получаемый при создании API ключа на бирже Bybit
   - _**withdraw_coin_ticker**_ - тикер монеты, которую будем выводить (можно посмотреть при добавлении адресов в вайтлист)
   - _**withdraw_network**_ - сеть, в которой будем выводить монеты (можно посмотреть при добавлении адресов в вайтлист)
   - _**account_type**_ - в зависимости от того, на каком счете находятся средства ("SPOT" / "FUND")
   - _**withdraw_min_amount**_ - минимальное количество монет на вывод на 1 кошелек
   - _**withdraw_max_amount**_ - максимальное количество монет на вывод на 1 кошелек
   - _**random_min_amount_digits**_ - минимальное количество цифр после запятой в количестве монет на вывод
   - _**random_max_amount_digits**_ - максимальное количество цифр после запятой в количестве монет на вывод
   - _**withdraw_min_delay_sec**_ - минимальная пауза перед следующим выводом (в секундах)
   - _**withdraw_max_delay_sec**_ - максимальная пауза перед следующим выводом (в секундах)
8. В терминале, находясь в папке проекта, вписываем команду "python3 bybit_bulk_withdrawal.py" и жмем ENTER.
9. Читаем информацию перед стартом в консоли и подтверждаем, вводя в консоль "y" (английская, игрек) и жмем ENTER.
10. Первый вывод производится сразу, после чего начинает работать задержка.

