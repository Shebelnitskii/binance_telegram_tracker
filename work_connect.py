from binance import Client
import pandas as pd
import os

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET_KEY")

client = Client(api_key, api_secret)
tickers = client.get_all_tickers()
for i in tickers:
    if i['symbol'] == 'BTCUSDT':
        print(i)
# print(tickers)
# deposits = client.get_his
# btc_deposits = client.get_deposit_history(coin='BTC')
# print(btc_deposits)
symbol = 'BTCUSDT'  # Валютная пара, данные которой вас интересуют
interval = Client.KLINE_INTERVAL_1DAY  # Интервал времени (например, 1 час)
start_time = "2023-01-01"  # Начальная дата и время в формате 'ГГГГ-ММ-ДД'
end_time = "2023-08-31"  # Конечная дата и время в формате 'ГГГГ-ММ-ДД'

# Получите исторические данные
historical_data = client.get_historical_klines(
    symbol, interval, start_time, end_time)

# Создайте DataFrame из полученных данных
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
           'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
df = pd.DataFrame(historical_data, columns=columns)

# Преобразуйте столбец timestamp в формат даты и времени
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Выведите полученные данные
print(df)
