# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import api_info
import pandas as pd
import os.path
from os import path
from binance.client import Client

# %%
client = Client(api_info.key, api_info.secret)

# %%
def save_historical_candles(symbol, interval, start_time, end_time) :
    file_name = symbol + "_" + interval + "_" + start_time + "_" + end_time + ".csv"
    
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
def get_historical_candles(symbol, interval, start_time, end_time) : 
    file_name = symbol + "_" + interval + "_" + start_time + "_" + end_time + ".csv"
    if ( path.exists(file_name) ) : 
        data = pd.read_csv(file_name)
        return data
    else : 
        data = save_historical_candles(symbol, interval, start_time, end_time) 
        return data
# %%
