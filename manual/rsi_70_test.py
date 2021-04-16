# %%
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

# %%
data = read_from_csv("BTCBUSD_2h.csv")
data.head()
