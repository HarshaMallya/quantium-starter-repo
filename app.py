import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1("Pink Morsel Sales Visualisation",
            style={'textAlign': 'center', 'color': '#2c3e50'}),

    # Radio buttons
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin': '10px'}
    ),

    dcc.Graph(id='sales-chart')

], style={'backgroundColor': '#ecf0f1', 'padding': '20px'})


# Callback
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):

    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title='Sales Over Time'
    )

    return fig


# Run app
if __name__ == '__main__':
    app.run(debug=True)