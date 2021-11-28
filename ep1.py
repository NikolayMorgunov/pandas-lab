import csv
import pandas as pd
import numpy as np
from inting import inting


with open('transactions.csv', 'r') as f:
    reader = np.array(list((csv.reader(f, delimiter=',', quotechar='\"'))))
    df = pd.DataFrame(reader[1:], columns=reader[0]).filter(items=['CONTRACTOR', 'STATUS', 'SUM'])
    df['SUM'] = pd.to_numeric(df['SUM'])
    df_is_ok = df[df['STATUS'] == "OK"].sort_values(by=['SUM']).tail(3).filter(items=['CONTRACTOR', 'SUM'])
    print("3 самых крупных платежа:")
    print(df_is_ok)

    df_is_ok = df[df['STATUS'] == "OK"]
    df_is_ok = df_is_ok[df_is_ok['CONTRACTOR'] == "Umbrella, Inc"]
    print('В адрес Umbrella, Inc было переведено', df_is_ok['SUM'].sum())
