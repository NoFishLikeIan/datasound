import csv
import numpy as np


def load_data(path='data/parsed.csv'):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield np.array(row).astype(float)


fetch_data_iter = load_data()
