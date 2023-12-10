from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import redis
import json

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
# print(df[df.country=='Canada'].to_dict())
# print(df[df.country=='Canada'])

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

redis_client = redis.Redis(host='192.168.121.66', port=6379, db=0, decode_responses=True)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='traffic-graph', style={'textAlign':'center'}),
    dcc.Graph(id='traffic-graph'),
    # html.H1(children='graph-content2', style={'textAlign':'center'}),
    # dcc.Graph(id='graph-content2'),
    # html.H1(children='graph-content3', style={'textAlign':'center'}),
    # dcc.Graph(id='graph-content3'),
    dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
    )
])

interval_graph_0 = 0
interval_graph_1 = 0
interval_graph_2 = 0

def update_interval_graph_0():
    global interval_graph_0
    interval_graph_0 = interval_graph_0 + 1

def update_interval_graph_1():
    global interval_graph_1
    interval_graph_1 = interval_graph_1 + 1

def update_interval_graph_2():
    global interval_graph_2
    interval_graph_2 = interval_graph_2 + 1

data_graph_0 = {'time(seconds)': {}, 'traffic': {}}
data_graph_1 = {'time(seconds)': {}, 'traffic': {}}
data_graph_2 = {'time(seconds)': {}, 'traffic': {}}

def update_data_graph_0(interval, x, y):
    global data_graph_0
    data_graph_0['time(seconds)'][interval] = x
    data_graph_0['traffic'][interval] = y

@callback(
    Output('traffic-graph', 'figure', ),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    if interval_graph_0 < 10:
        print("Still gathering data for traffic graph: " + str(data_graph_0))
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_0(interval_graph_0, interval_graph_0 * 5, metrics_dict['traffic'])
        update_interval_graph_0()
        return {}
    else:
        dff = pd.DataFrame(data_graph_0)
        print(dff)
        return px.line(dff, x='time(seconds)', y='traffic')

# @callback(
#     Output('graph-content2', 'figure'),
#     Input('interval-component', 'n_intervals')
# )
# def update_graph1(n):
#     print("intervals from graph 1: " + str(interval_graph_1))
#     update_interval_graph_1()
#     dff = df[df.country=='Afghanistan']
#     return px.line(dff, x='year', y='pop')

# @callback(
#     Output('graph-content3', 'figure'),
#     Input('interval-component', 'n_intervals')
# )
# def update_graph2(n):
#     print("intervals from graph 2: " + str(interval_graph_2))
#     update_interval_graph_2()
#     dff = df[df.country=='Zimbabwe']
#     return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=31216)