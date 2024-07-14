import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data
stock = yf.Ticker("AAPL")
hist = stock.history(period="1y")

# Plot candlestick chart
plt.figure(figsize=(10, 6))
plt.plot(hist.index, hist['Close'], label='Close Price')
plt.plot(hist.index, hist['Close'].rolling(window=50).mean(), label='50-Day MA')
plt.plot(hist.index, hist['Close'].rolling(window=200).mean(), label='200-Day MA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AAPL Stock Price')
plt.legend()
plt.show()
