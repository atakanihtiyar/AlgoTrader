# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import config
from binance.client import Client

# %%
client = Client(config.api_key, config.api_secret)
