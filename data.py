import pandas as pd
import plotly.express as px
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)
MyData = pd.read_csv('data1.csv')
print (MyData)
figure = px.scatter(MyData, x = 'date', y = 'cases',color='country')
figure.show()