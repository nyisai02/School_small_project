import pandas as pd
from sma.Table import table_data
from sma.SMA import calculate_sma
from sma.MSE import calculate_mse
from sma.SSE import calculate_sse
from sma.SES import calculate_ses

data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
period = 3

def main():
    sma = calculate_sma(data, period)
    mse = calculate_mse(data, sma)
    sse = calculate_sse(data, sma)
    ses = calculate_ses(data, sse)
    df = table_data(data, sma, mse, sse, ses)
    print(df)

if __name__ == '__main__':
    main()