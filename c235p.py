import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('projectC234_EPL.csv')

footballclub = dataset['Club'].value_counts().head(20)

print("Top 10 Clubs with Penalty \n",footballclub)

club_fig = go.Figure(data=[go.Pie(labels=footballclub.index,values = footballclub.values,hole = 0.5)])
club_fig.show()