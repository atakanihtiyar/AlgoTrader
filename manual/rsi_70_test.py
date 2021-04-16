# %%
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

# %%
get_historical_candles("BTCBUSD", "2h", "September 01, 2017", "September 01, 2020")
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
sma_30 = pd.Dataframe()
sma_30["Close price"]