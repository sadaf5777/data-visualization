
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
df=pd.read_csv(r"C:\Users\Nadeem Anwar\Desktop\Sadaf\week9 data visualization\dash app\gapminde.csv")
app=dash.Dash(__name__)
app.layout=html.Div([
    html.H1("DASHBOARD",style={"color":"red","text-align":"center"}),
    html.Div(style={'border':"1 px black solid",'float':"left","width":"100%","height":"50px"}),
    html.Div(style={'border':"1 px black solid",'float':"left","width":"49.9%","height":"350px"}),
    html.Div(style={'border':"1 px black solid",'float':"left","width":"49.9%","height":"350px"})

])

if __name__=="__main__":
    app.run(debug=True)