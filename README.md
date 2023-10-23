# Project-Matplotlib-Options-PnL-Visualizer

A aggregated PnL visualizer for multiple option positions. For my own option trading use.

## Introduction

A simple visualizer to aggregate the PnL for multiple options hand within a given expiration price range.

Since I am an option trader myself, and I only trades delta-neutral strategies, this is a good visualzier for strategies crafting.

## How to run

Make sure you have python and matplotlib installed in your computer.

Git clone the repo.

Edit the CURRENT_SPOT_PRICE and CURRENT_OPTION_POSITIONS to reflect your option positions.

Option positions were presented in a python list/array. Every option is a position following below format:

```python
{'type': 'Call', 'action': 'sell', 'strike': 1975, 'premium': 42, 'quantity': 1}
```

To run:

```shell
python main.py
```

## Key Concepts Beforehand

- Options Trading

  - Understanding what is option, how option works
  - Understanding Delta, Vega and Theta in option trading
  - Understanding the premium and its decay upon apporaching expiration

- Matplotlib
  - Understand how to use Matplotlib to plot a graph
