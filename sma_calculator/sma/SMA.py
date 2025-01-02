import pandas as pd
import numpy as np
def calculate_sma(prices, period):
    return prices.rolling(window=period).mean()
