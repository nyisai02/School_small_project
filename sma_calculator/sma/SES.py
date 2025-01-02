import numpy as np
def calculate_ses(prices, sse):
    return np.sum((prices - sse) ** 2)
