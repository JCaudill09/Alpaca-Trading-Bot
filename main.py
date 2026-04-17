def get_account_buying_power():
    # Retrieve the available cash from the account
    # Replace the logic below with the actual API call to get the account balance
    account_info = api.get_account()
    return float(account_info.cash)

def calculate_order_amount():
    available_balance = get_account_buying_power()
    if available_balance < 30:
        return 0
    elif available_balance < 50:
        return available_balance
    else:
        return 50

def place_50_dollar_order():
    order_amount = calculate_order_amount()
    if order_amount > 0:
        # Place buy order with the calculated amount
        api.submit_order(
            symbol='AAPL',
            qty=order_amount,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
