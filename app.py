import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import numpy as np


tesla=yf.Ticker('TSLA')
tesla_data=tesla.history(period='max')
tesla_data.reset_index(inplace=True)
tesla_data.to_csv('tesla_data.csv')

gme=yf.Ticker('GME')
gme_data=gme.history(period='max')
gme_data.reset_index(inplace=True)
gme_data.to_csv('GME_data.csv')
print(gme_data.tail())

plt.figure(figsize=(14, 7))
plt.plot(gme_data['Close'])
plt.title('Tesla Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()

