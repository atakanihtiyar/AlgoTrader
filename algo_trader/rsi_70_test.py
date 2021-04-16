# %%
import pandas as pd
import binance_client as cl
import pandas_ta as ta
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