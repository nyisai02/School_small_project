import numpy as np
def calculate_mse(prices, sma):
    return np.mean((prices - sma) ** 2)
