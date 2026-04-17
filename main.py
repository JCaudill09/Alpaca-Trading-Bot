import alpaca_trade_api as tradeapi
import time

# Replace these variables with your Alpaca API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Connect to the market
while True:
    try:
        account = api.get_account()
        print('Connected to Alpaca API')
        break
    except Exception as e:
        print('Connection failed, retrying...')
        time.sleep(5)

# Function to place an order

def place_order(symbol, qty, side, order_type='market', time_in_force='gtc'):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=order_type,
            time_in_force=time_in_force
        )
        print(f'Placed {side} order for {qty} shares of {symbol}')
    except Exception as e:
        print(f'Error placing order: {e}')

# Example trading strategy: Buy if price is low, sell if price is high

def trading_logic():
    symbol = 'AAPL'
    qty = 10
    # Simple example conditions
    current_price = api.get_last_trade(symbol).price
    if current_price < 150:
        place_order(symbol, qty, 'buy')
    elif current_price > 160:
        place_order(symbol, qty, 'sell')

# Main trading loop
while True:
    trading_logic()
    time.sleep(60)  # Wait for 60 seconds before checking again