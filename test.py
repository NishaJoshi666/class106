import pandas as pd
import plotly.express as px
import csv
import numpy as np

# df = pd.read_csv('106data1.csv')
# fig = px.scatter(df,x='Temperature',y='Ice-cream Sales( ₹ )')

# fig.show()

def getDataSource(datapath):
  IceCreamSales = []
  Temperature = []
  with open(datapath) as r:
    csvreader = csv.DictReader(r)
    for row in csvreader:
      IceCreamSales.append(float[row["Ice-cream Sales( ₹ )"]])
      Temperature.append(float[row["Temperature"]])

  return{"x":IceCreamSales,"y":Temperature}

def correlation(DataSource):
  corr = np.corrcoef(DataSource["x"],DataSource["y"])
  print("Correaltion between temperature and icecream sales: ",corr)

def setup():
  Datapath = "106data1.csv"
  DataSource1 = getDataSource(datapath)
  correlation(DataSource1)

setup()