import csv
import pandas as pd
import numpy as np
from inting import inting
import matplotlib.pyplot as plt

with open('flights.csv', 'r') as f:
    reader = np.array(list((csv.reader(f, delimiter=',', quotechar='\"'))))
    df = pd.DataFrame(reader[1:], columns=reader[0]).filter(items=['CARGO', 'PRICE', 'WEIGHT'])
    df['PRICE'] = pd.to_numeric(df['PRICE'])
    df['WEIGHT'] = pd.to_numeric(df['WEIGHT'])
    number = [1 for i in range(len(df))]
    df['NUMBER'] = number
    df = df.groupby('CARGO').sum()

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].set_title("Flights per cargo")
    axs[0, 0].bar(df.index[:], df['NUMBER'], color='blue')

    axs[1, 0].set_title("Price per cargo")
    axs[1, 0].bar(df.index[:], df['PRICE'], color='green')

    axs[0, 1].set_title("Weight per cargo")
    axs[0, 1].bar(df.index[:], df['WEIGHT'], color='red')

    axs[1, 1].axis('off')
    plt.show()
