import random
import pandas as pd
import plotly.express as px
import statistics
import plotly.figure_factory as ff
result = []
df = pd.read_csv("data.csv")
result = df["average"].tolist()
mean = sum(result)/len(result)
print (mean)
median = statistics.median(result)
print (median)
mode = statistics.mode(result)
print (mode)
std = statistics.stdev(result)
print (std)