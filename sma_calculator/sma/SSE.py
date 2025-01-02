import numpy as np
def calculate_sse(prices, sma):
    return np.sum((prices - sma) ** 2)