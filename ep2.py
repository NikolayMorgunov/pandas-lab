import csv
import pandas as pd
import numpy as np
from inting import inting
import matplotlib.pyplot as plt


with open('flights.csv', 'r') as f:
    reader = np.array(list((csv.reader(f, delimiter=',', quotechar='\"'))))
    df = pd.DataFrame(reader[1:], columns=reader[0]).filter(items=['CARGO', 'PRICE', 'WEIGHT']).applymap(inting)

    cargos = set()
    for ind, i in df.iterrows():
        cargos.add(i['CARGO'])

    cargos = list(cargos)
    flights = []
    prises = []
    weights = []
    for i in cargos:
        cargo_is_concr = df[df['CARGO'] == i]
        flights.append(len(cargo_is_concr))
        prises.append(cargo_is_concr['PRICE'].sum())
        weights.append(cargo_is_concr['WEIGHT'].sum())

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].set_title("Flights per cargo")
    axs[0, 0].bar(cargos, flights, color='blue')

    axs[1, 0].set_title("Price per cargo")
    axs[1, 0].bar(cargos, prises, color='red')

    axs[0, 1].set_title("Weight per cargo")
    axs[0, 1].bar(cargos, weights, color='green')

    axs[1, 1].axis('off')
    plt.show()


