# filename: stock_price_chart.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbols
stock_symbols = ['NVDA', 'AAPL', 'TSLA']

# Fetch the stock price data
stock_data = yf.download(stock_symbols, start="2022-01-01", end=pd.to_datetime('today'))

# Extract the adjusted close prices
stock_prices = stock_data['Adj Close']

# Plot the stock price change YTD
stock_prices.plot(figsize=(10, 7))
plt.title('Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend(stock_symbols)

# Save the plot as an image file
plt.savefig('stock_price_change_ytd.png')

# Display the plot
plt.show()