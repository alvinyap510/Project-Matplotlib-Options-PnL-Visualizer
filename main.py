'''
Plotting the profit and loss range upon expiration
for given multiple options in hand.
'''

import matplotlib.pyplot as plt

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
CURRENT_SPOT_PRICE = 1974
CURRENT_OPTION_POSITIONS = [
    {'type': 'Call', 'action': 'sell', 'strike': 1965, 'premium': 54, 'quantity': 1},
    {'type': 'Put', 'action': 'sell', 'strike': 1990, 'premium': 44, 'quantity': 1},
    {'type': 'Put', 'action': 'buy', 'strike': 1930, 'premium': 16, 'quantity': 1},
    {'type': 'Call', 'action': 'buy', 'strike': 2020, 'premium': 17.50, 'quantity': 1}
]


def calculate_premium_received(option_positions):
    '''
    Calculatte the premium received upfront minus
    the cost of purchasing options.
    '''
    premium = 0
    for option in option_positions:
        if option['action'] == 'sell':
            premium += option['premium']
        elif option['action'] == 'buy':
            premium -= option['premium']
    return premium


def total_pnl(upfront_premium, price_point, options):
    '''
    Calculate the aggregated PnL upon expiration on
    a given spot price on expiration date
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
            pnl += option_value
        elif option['action'] == 'sell':
            pnl -= option_value
    return pnl


def visualize_pnl(spot_price, options, nett_premium):
    '''
    Plot the aggregated profit and loss range for
    the option positions
    '''
    # Get price range to plot
    prices = range(int(spot_price * (1 - PLOT_RANGE)),
                   int(spot_price * (1 + PLOT_RANGE)))

    # Get PnL on every price point
    pnls = [total_pnl(nett_premium, price_point, options)
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

    # Calculate the nett premium received upfront
    NETT_PREMIUM_RECEIVED = calculate_premium_received(
        CURRENT_OPTION_POSITIONS)

    # Visualize the PnL using Matplotlib
    visualize_pnl(SPOT_PRICE, OPTIONS, NETT_PREMIUM_RECEIVED)
