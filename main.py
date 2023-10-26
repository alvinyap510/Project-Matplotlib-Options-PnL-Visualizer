# pylint: disable=too-many-arguments
# pylint: disable=R0903
'''
Plotting the profit and loss range upon expiration
for given multiple options in hand.
'''

import matplotlib.pyplot as plt


class Option:
    '''
    Option Class
    '''

    def __init__(self, type_, action, strike, premium, quantity=1):
        self.type = type_
        self.action = action
        self.strike = strike
        self.premium = premium
        self.quantity = quantity

    def __getitem__(self, key):
        return getattr(self, key)


class Futures:
    '''
    Futures Class
    '''

    def __init__(self, _direction, _price, _quantity):
        self.direction = _direction
        self.price = _price
        self.quantity = _quantity

    def __getitem__(self, key):
        return getattr(self, key)


PLOT_RANGE = 0.05

# CURRENT_SPOT_PRICE = 1978
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 1965, 'premium': 33, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 1990, 'premium': 20, 'quantity': 1}
# ]

# # In-The-Money
# CURRENT_SPOT_PRICE = 1974
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 1960, 'premium': 51, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 1985, 'premium': 38, 'quantity': 1}
# ]

# # # At-The-Money
# CURRENT_SPOT_PRICE = 1974
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 1975, 'premium': 42, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 1975, 'premium': 32, 'quantity': 1}
# ]

# # Out-Of-Money
# CURRENT_SPOT_PRICE = 1974
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 1985, 'premium': 37, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 1960, 'premium': 25, 'quantity': 1}
# ]

# # Insurance
# CURRENT_SPOT_PRICE = 1974
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 1965, 'premium': 54, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 1990, 'premium': 44, 'quantity': 1},
#     {'type': 'Put', 'action': 'buy', 'strike': 1930, 'premium': 16, 'quantity': 1},
#     {'type': 'Call', 'action': 'buy', 'strike': 2020, 'premium': 17.50, 'quantity': 1}
# ]


# CURRENT_SPOT_PRICE = 17032
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 16800, 'premium': 480, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 17200, 'premium': 273, 'quantity': 1},
#     {'type': 'Call', 'action': 'buy', 'strike': 17200, 'premium': 0, 'quantity': 1},

# ]

# CURRENT_SPOT_PRICE = 138
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Call', 'action': 'sell', 'strike': 138, 'premium': 5.5, 'quantity': 1},
#     {'type': 'Put', 'action': 'sell', 'strike': 138, 'premium': 5, 'quantity': 1},
#     # {'type': 'Call', 'action': 'buy', 'strike': 180, 'premium': 2.34, 'quantity': 1},
#     # {'type': 'Put', 'action': 'buy', 'strike': 160, 'premium': 1.55, 'quantity': 1},
# ]

# CURRENT_SPOT_PRICE = 1972
# CURRENT_OPTION_POSITIONS = [
#     {'type': 'Put', 'action': 'sell', 'strike': 1985, 'premium': 41, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1960,
#         'premium': 44.84, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1965,
#              'premium': 48.50, 'quantity': 10},
#     {'type': 'Put', 'action': 'sell', 'strike': 1990,
#      'premium': 38.18, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1970,
#      'premium': 43.28, 'quantity': 10},
#     {'type': 'Put', 'action': 'sell', 'strike': 1995,
#      'premium': 41.70, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1990,
#      'premium': 27.62, 'quantity': 10},
#     {'type': 'Put', 'action': 'sell', 'strike': 1950,
#      'premium': 19.80, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1975,
#      'premium': 31.99, 'quantity': 10},
#     {'type': 'Put', 'action': 'sell', 'strike': 1950,
#      'premium': 20.47, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1965,
#      'premium': 41.32, 'quantity': 10},
#     {'type': 'Put', 'action': 'sell', 'strike': 1985,
#      'premium': 33.33, 'quantity': 10},
#     {'type': 'Call', 'action': 'sell', 'strike': 1960,
#      'premium': 43.11, 'quantity': 20},
#     {'type': 'Put', 'action': 'sell', 'strike': 1960,
#      'premium': 21.28, 'quantity': 20},
#     {'type': 'Call', 'action': 'sell', 'strike': 1980,
#      'premium': 33.60, 'quantity': 20},
#     {'type': 'Put', 'action': 'sell', 'strike': 1955,
#      'premium': 18.24, 'quantity': 20},
# ]

CURRENT_SPOT_PRICE = 1989
CURRENT_OPTION_POSITIONS = [
    Option("Put", "sell", 1985, 41, 10),
    Option("Call", "sell", 1960, 44.84, 10),
    Option("Call", "sell", 1965, 48.50, 10),
    Option("Put", "sell", 1990, 38.18, 10),
    Option("Call", "sell", 1970, 43.28, 10),
    Option("Put", "sell", 1995, 41.70, 10),
    Option("Call", "sell", 1990, 27.62, 10),
    Option("Put", "sell", 1950, 19.80, 10),
    Option("Call", "sell", 1975, 31.99, 10),
    Option("Put", "sell", 1950, 20.47, 10),
    Option("Call", "sell", 1965, 41.32, 10),
    Option("Put", "sell", 1985, 33.33, 10),
    Option("Call", "sell", 1960, 43.11, 20),
    Option("Put", "sell", 1960, 21.28, 20),
    Option("Call", "sell", 1980, 33.60, 20),
    Option("Put", "sell", 1955, 18.24, 20),
    Option("Call", "sell", 1980, 32.34, 20),
    Option("Call", "sell", 1980, 31.70, 10),
    Option("Put", "sell", 1960, 20.50, 20),
    Option("Put", "sell", 1960, 20.50, 10),
    Option("Call", "sell", 2000, 31.51, 10),
    Option("Call", "sell", 1975, 43.62, 10),
    Option("Put", "sell", 2000, 35.96, 10),
    Option("Call", "sell", 1975, 45.38, 10),
    Option("Put", "sell", 2000, 34.99, 10),
    Option("Put", "sell", 2000, 34.90, 10),
    Option("Call", "sell", 1975, 46.24, 10),
    Option("Put", "sell", 2000, 35.49, 10),
]

CURRENT_FUTURES_POSITIONS = [
    Futures("long", 1990, 100),
    Futures("short", 1960, 100)
]


def calculate_premium_received(option_positions):
    '''
    Calculatte the premium received upfront minus
    the cost of purchasing options.
    '''
    premium = 0
    for option in option_positions:
        if option['action'] == 'sell':
            premium += option['premium'] * option['quantity']
        elif option['action'] == 'buy':
            premium -= option['premium'] * option['quantity']
    return premium


def calculate_futures_pnl(entry_price, current_price, quantity, direction):
    """
    Calculate the PnL for a futures position given an entry price, current price,
    the quantity of contracts, and the direction (long or short).
    """
    if direction == "long":
        return (current_price - entry_price) * quantity
    if direction == "short":
        return (entry_price - current_price) * quantity
    raise ValueError("Invalid direction. Expected 'long' or 'short'.")


def total_pnl(upfront_premium, price_point, options, futures):
    '''
    Calculate the aggregated PnL upon expiration on
    a given spot price on expiration date, including futures positions
    '''
    pnl = upfront_premium
    for option in options:
        # Call options
        if option['type'] == 'Call':
            # Determine option value
            if option['strike'] >= price_point:
                option_value = 0
            else:
                option_value = price_point - option['strike']
        # Put options
        if option['type'] == 'Put':
            # Determine option value
            if option['strike'] <= price_point:
                option_value = 0
            else:
                option_value = option['strike'] - price_point
        # Determine whether user sold the option or purchased the option
        if option['action'] == 'buy':
            pnl += option_value * option['quantity']
        elif option['action'] == 'sell':
            pnl -= option_value * option['quantity']
        # Include futures PnL
    for future in futures:
        pnl += calculate_futures_pnl(
            future['price'], price_point, future['quantity'], future['direction']
        )

    return pnl


def visualize_pnl(spot_price, options, nett_premium, futures):
    '''
    Plot the aggregated profit and loss range for
    the option positions
    '''
    # Get price range to plot
    prices = range(int(spot_price * (1 - PLOT_RANGE)),
                   int(spot_price * (1 + PLOT_RANGE)))

    # Get PnL on every price point
    pnls = [total_pnl(nett_premium, price_point, options, futures)
            for price_point in prices]

    # Title of the graph
    plt.title("Aggregated Options Profit-Loss Range")

    # Labeing x-axis and y-axis
    plt.xlabel("Spot Price Upon Options Expiration")
    plt.ylabel("Profit / Loss")

    # # Plot the x-axis and y-axis
    # plt.plot(prices, pnls)

    # Loop through prices and plot line segments in the appropriate color
    for i in range(1, len(prices)):
        color = 'green' if pnls[i-1] >= 0 else 'red'
        plt.plot(prices[i-1:i+1], pnls[i-1:i+1], color=color)

    # Plot the 0 profit line
    plt.axhline(0, color='black', linewidth=0.5)
    # Plot the current spot price
    plt.axvline(spot_price, color='orange', linestyle='--',
                label='Opening Spot Price')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # The current spot price and option positions
    SPOT_PRICE = CURRENT_SPOT_PRICE
    OPTIONS = CURRENT_OPTION_POSITIONS
    FUTURES = CURRENT_FUTURES_POSITIONS

    # Calculate the nett premium received upfront
    NETT_PREMIUM_RECEIVED = calculate_premium_received(
        CURRENT_OPTION_POSITIONS)

    # Visualize the PnL using Matplotlib
    visualize_pnl(SPOT_PRICE, OPTIONS, NETT_PREMIUM_RECEIVED, FUTURES)
