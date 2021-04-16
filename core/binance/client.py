# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import config
import pandas as pd
from binance.client import Client

# %%
client = Client(config.api_key, config.api_secret)

# %%
def save_historical_candles(symbol, interval, start_time, end_time) :
    file_name = symbol + "_" + interval + ".csv"
    
    columns_name = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", 
            "Quote asset volume", "Number of trades", "Taker buy base asset volume", 
            "Taker buy quote asset volume", "Can be ignored"]
    
    data_json = client.get_historical_klines(symbol, interval, start_time, end_time)
    
    data = pd.DataFrame(data_json, columns = columns_name)
    data['Close time'] = pd.to_datetime(data['Close time'], unit='ms')
    data['Open time'] = pd.to_datetime(data['Open time'], unit='ms')
    data.to_csv(file_name, encoding='utf-8')

    return(data)

# %%
