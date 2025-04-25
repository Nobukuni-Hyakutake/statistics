# Ctrl+Cで終了する

import dash
from dash import dcc
from dash import html
import plotly.express as px

app = dash.Dash(__name__)

app.layout=dcc.Graph(
  figure=px.bar(x=[1,2,3,4,5],y=[1,2,3,4,5])
)

if __name__=="__main__":
    app.run(debug=True)
