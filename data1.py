import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px
df = pd.read_csv('data.csv')
fig = go.Figure(go.Bar(x = df.groupby('level')['attempt'].mean()
,y = ['Level 1','Level 2', 'Level 3', 'Level 4'], orientation = 'h'))
fig.show()
fig1 = px.scatter(df.groupby('level')['attempt'].mean(), x = 'student_id'
,y = 'Levels', size = 'attempt', color = 'attempt')