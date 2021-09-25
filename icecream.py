import plotly.express as px
import csv 
with open("temp.csv") as csv_file:
    df = csv.DictReader(csv_file)
    figure = px.scatter(df, x = "temp", y = "icecream")
    figure.show()