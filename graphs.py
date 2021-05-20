import plotly.express as px
import csv
import numpy as np
import pandas as pd

def data():
    temp = []
    sales = []
    with open("icecreamdata.csv") as data:
        df = csv.DictReader(data)
        for row in df:
            temp.append(float(row['Temperature']))
            sales.append(float(row['Ice-cream Sales']))
        return {'x': temp, 'y': sales}

def correlate():
    datasrc = data()
    correlation = np.corrcoef(datasrc['x'], datasrc['y'])
    print(correlation[0, 1])

def plot():
    f = pd.read_csv('icecreamdata.csv')
    graph = px.scatter(f, x="Temperature", y = "Ice-cream Sales", size = "Ice-cream Sales")
    graph.show()

correlate()
input("Do you want to see a graph? ")
if input == "yes":
    plot()