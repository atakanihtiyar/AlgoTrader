# %%
import binance_client as cl
import pandas as pd
import pandas_ta as ta
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

# %%
data = cl.get_historical_candles("BTCUSDT", "2h", "September 01, 2017", "September 01, 2020")
data.head()

# %%
plt.figure(figsize=(12.5, 4.5))
plt.plot(data["Close"], label = "BTC - BUSD")
plt.title("")
plt.xlabel(data.iloc[0]["Close time"] + " between " + data.iloc[-1]["Close time"])
plt.ylabel("BTC close prices(USD)")
plt.legend(loc = "upper left")
plt.show()

# %%
sma_9 = pd.DataFrame()
sma_9["Close"] = ta.sma(data["Close"], 9)
sma_9
# %%
sma_100 = pd.DataFrame()
sma_100["Close"] = ta.sma(data["Close"], 100)
sma_100
# %%
rsi_14 = pd.DataFrame()
rsi_14["Close"] = ta.rsi(data["Close"], 14)
rsi_14

# %%
plt.figure(figsize=(12.5, 4.5))
plt.plot(data["Close"], label = "BTC - BUSD")
plt.plot(sma_9["Close"], label = "SMA 9")
plt.plot(sma_100["Close"], label = "SMA 100")
plt.plot(rsi_14["Close"], label = "RSI 14")
plt.title("")
plt.xlabel(data.iloc[0]["Close time"] + " between " + data.iloc[-1]["Close time"])
plt.ylabel("BTC close prices(USD)")
plt.legend(loc = "upper left")
plt.show()

# %%
results = pd.DataFrame()
results['BTC'] = data["Close"]
results['SMA 9'] = sma_9["Close"]
results['SMA 100'] = sma_100["Close"]
results['RSI 14'] = rsi_14["Close"]
results
# %%
def decision(data) : 
    signal_price_buy = []
    signal_price_sell = []
    nextOrder = "buy"

    for i in range(len(data)) : 
        if (data["BTC"][i] > data["SMA 100"][i] and data["RSI 14"][i] > 70) : 
            if (nextOrder == "buy") : 
                signal_price_buy.append(data["BTC"][i])
                signal_price_sell.append(np.nan)
                nextOrder = "sell"
            else : 
                signal_price_buy.append(np.nan)
                signal_price_sell.append(np.nan)
        
        elif (data["BTC"][i] < data["SMA 9"][i] or data["SMA 9"][i] < data["SMA 100"][i]) : 
            if (nextOrder == "sell") : 
                signal_price_buy.append(np.nan)
                signal_price_sell.append(data["BTC"][i])
                nextOrder = "buy"
            else : 
                signal_price_buy.append(np.nan)
                signal_price_sell.append(np.nan)
        
        else :
            signal_price_buy.append(np.nan)
            signal_price_sell.append(np.nan)

    return (signal_price_buy, signal_price_sell)

# %%
decisions = decision(results)
results["Buy Signal"] = decisions[0]
results["Sell Signal"] = decisions[1]

# %%
results

# %%
plt.figure(figsize=(12.5, 4.5))
plt.plot(data["Close"], label = "BTC - BUSD")
plt.plot(sma_9["Close"], label = "SMA 9")
plt.plot(sma_100["Close"], label = "SMA 100")
plt.plot(rsi_14["Close"], label = "RSI 14")
plt.scatter(results.index, results["Buy Signal"], label = "Buy", marker = "^", color = "green")
plt.scatter(results.index, results["Sell Signal"], label = "Sell", marker = "v", color = "red")
plt.title("")
plt.xlabel(data.iloc[0]["Close time"] + " between " + data.iloc[-1]["Close time"])
plt.ylabel("BTC close prices(USD)")
plt.legend(loc = "upper left")
plt.show()