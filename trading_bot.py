import alpaca_trade_api as tradeapi
import time

# Insert your Alpaca API credentials here
API_KEY = 'PKR6GIVN5X26BQIWMEDVZDIH4F'
API_SECRET = 'Fu5bTb4BhoVBRwQLeDBPWNV9AnaxPhzenTkXyGqmFkkc'
BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Define the stock to trade
symbol = 'AAPL'

# Define the take profit and stop loss percentages
TAKE_PROFIT = 0.075
STOP_LOSS = 0.025

def place_order(symbol, qty):
    # Place a market order
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

    # Get the current price of the stock
    current_price = api.get_last_trade(symbol).price

    # Calculate take profit and stop loss prices
    take_profit_price = current_price * (1 + TAKE_PROFIT)
    stop_loss_price = current_price * (1 - STOP_LOSS)

    # Use Alpaca's oco_order feature to place take profit and stop loss orders
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='oco',
        time_in_force='gtc',
        stop_price=stop_loss_price,
        limit_price=take_profit_price,
        client_order_id='take_profit_and_stop_loss'
    )

# Example usage: Place an order for 1 share of AAPL
if __name__ == '__main__':
    place_order(symbol, 1)