# from dash import Dash,html,dcc,Input
# from dash.dependencies import Input,Output

# app=Dash(__name__)
# app.layout=html.Div([
#    html.Button('Submit',id='number'),
#    dcc.Input(placeholder="Enter a valid number",id='Data',type='number'),
#    html.H1(id='Result')
#    ])
# @app.callback(Output('Result','children'),
#               Input('number','n_clicks'))
# def play_data(n,data):
#    if n:
#       return f"your enter:{data}"
#    return ""
# app.run(debug=True)

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_excel(
    'D:/DEPI/Amit/Amit/data_analysis/In-Sessions/data_sets/Dash.xlsx'
)

app = Dash(__name__)
app.title = "Interactive Dashboard"

num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("Interactive Dashboard with Pie Chart"),

    html.Label("Select a value to show the pie chart"),

    dcc.Dropdown(
        id='column-dropdown',   
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0]
    ),

    dcc.Graph(id='pie-chart')
])

@app.callback(
    Output('pie-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_pie(selected_col):
    grouped = df.groupby('Area')[selected_col].sum().reset_index()

    fig = px.pie(
        grouped,
        names='Area',
        values=selected_col,
        title=f"Distribution of {selected_col} by Area",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)


