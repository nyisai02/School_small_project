import pandas as pd
import numpy as np

def table_data(data, sma, mse, sse, ses):
    df = pd.DataFrame({'Data': data, 'SMA': sma, 'MSE': mse, 'SSE': sse, 'SES': ses})
    return df