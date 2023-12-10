from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import redis
import json

redis_client = redis.Redis(host='192.168.121.66', port=6379, db=0, decode_responses=True)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='traffic-graph', style={'textAlign':'center'}),
    dcc.Graph(id='traffic-graph'),
    html.H1(children='memory-graph', style={'textAlign':'center'}),
    dcc.Graph(id='memory-graph'),
    html.H1(children='cpu-0-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-0-graph'),
    html.H1(children='cpu-1-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-1-graph'),
    html.H1(children='cpu-2-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-2-graph'),
    html.H1(children='cpu-3-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-3-graph'),
    html.H1(children='cpu-4-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-4-graph'),
    html.H1(children='cpu-5-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-5-graph'),
    html.H1(children='cpu-6-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-6-graph'),
    html.H1(children='cpu-7-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-7-graph'),
    html.H1(children='cpu-8-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-8-graph'),
    html.H1(children='cpu-9-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-9-graph'),
    html.H1(children='cpu-10-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-10-graph'),
    html.H1(children='cpu-11-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-11-graph'),
    html.H1(children='cpu-12-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-12-graph'),
    html.H1(children='cpu-13-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-13-graph'),
    html.H1(children='cpu-14-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-14-graph'),
    html.H1(children='cpu-15-graph', style={'textAlign':'center'}),
    dcc.Graph(id='cpu-15-graph'),
    dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
    )
])


#################### INTERVALOS ####################

interval_graph_0 = 0
interval_graph_1 = 0
interval_graph_2 = 0
interval_graph_3 = 0
interval_graph_4 = 0
interval_graph_5 = 0
interval_graph_6 = 0
interval_graph_7 = 0
interval_graph_8 = 0
interval_graph_9 = 0
interval_graph_10 = 0
interval_graph_11 = 0
interval_graph_12 = 0
interval_graph_13 = 0
interval_graph_14 = 0
interval_graph_15 = 0
interval_graph_16 = 0
interval_graph_17 = 0

def update_interval_graph_0():
    global interval_graph_0
    interval_graph_0 = interval_graph_0 + 1

def update_interval_graph_1():
    global interval_graph_1
    interval_graph_1 = interval_graph_1 + 1

def update_interval_graph_2():
    global interval_graph_2
    interval_graph_2 = interval_graph_2 + 1

def update_interval_graph_3():
    global interval_graph_3
    interval_graph_3 = interval_graph_3 + 1

def update_interval_graph_4():
    global interval_graph_4
    interval_graph_4 = interval_graph_4 + 1

def update_interval_graph_5():
    global interval_graph_5
    interval_graph_5 = interval_graph_5 + 1

def update_interval_graph_6():
    global interval_graph_6
    interval_graph_6 = interval_graph_6 + 1

def update_interval_graph_7():
    global interval_graph_7
    interval_graph_7 = interval_graph_7 + 1

def update_interval_graph_8():
    global interval_graph_8
    interval_graph_8 = interval_graph_8 + 1

def update_interval_graph_9():
    global interval_graph_9
    interval_graph_9 = interval_graph_9 + 1

def update_interval_graph_10():
    global interval_graph_10
    interval_graph_10 = interval_graph_10 + 1

def update_interval_graph_11():
    global interval_graph_11
    interval_graph_11 = interval_graph_11 + 1

def update_interval_graph_12():
    global interval_graph_12
    interval_graph_12 = interval_graph_12 + 1

def update_interval_graph_13():
    global interval_graph_13
    interval_graph_13 = interval_graph_13 + 1

def update_interval_graph_14():
    global interval_graph_14
    interval_graph_14 = interval_graph_14 + 1

def update_interval_graph_15():
    global interval_graph_15
    interval_graph_15 = interval_graph_15 + 1

def update_interval_graph_16():
    global interval_graph_16
    interval_graph_16 = interval_graph_16 + 1

def update_interval_graph_17():
    global interval_graph_17
    interval_graph_17 = interval_graph_17 + 1


#################### DADOS ####################

data_graph_0 = {'time(seconds)': {}, 'traffic': {}}
data_graph_1 = {'time(seconds)': {}, 'memory': {}}
data_graph_2 = {'time(seconds)': {}, 'cpu-0': {}}
data_graph_3 = {'time(seconds)': {}, 'cpu-1': {}}
data_graph_4 = {'time(seconds)': {}, 'cpu-2': {}}
data_graph_5 = {'time(seconds)': {}, 'cpu-3': {}}
data_graph_6 = {'time(seconds)': {}, 'cpu-4': {}}
data_graph_7 = {'time(seconds)': {}, 'cpu-5': {}}
data_graph_8 = {'time(seconds)': {}, 'cpu-6': {}}
data_graph_9 = {'time(seconds)': {}, 'cpu-7': {}}
data_graph_10 = {'time(seconds)': {}, 'cpu-8': {}}
data_graph_11 = {'time(seconds)': {}, 'cpu-9': {}}
data_graph_12 = {'time(seconds)': {}, 'cpu-10': {}}
data_graph_13 = {'time(seconds)': {}, 'cpu-11': {}}
data_graph_14 = {'time(seconds)': {}, 'cpu-12': {}}
data_graph_15 = {'time(seconds)': {}, 'cpu-13': {}}
data_graph_16 = {'time(seconds)': {}, 'cpu-14': {}}
data_graph_17 = {'time(seconds)': {}, 'cpu-15': {}}

def update_data_graph_0(interval, x, y):
    global data_graph_0
    data_graph_0['time(seconds)'][interval] = x
    data_graph_0['traffic'][interval] = y

def update_data_graph_1(interval, x, y):
    global data_graph_1
    data_graph_1['time(seconds)'][interval] = x
    data_graph_1['memory'][interval] = y

def update_data_graph_2(interval, x, y):
    global data_graph_2
    data_graph_2['time(seconds)'][interval] = x
    data_graph_2['cpu-0'][interval] = y

def update_data_graph_3(interval, x, y):
    global data_graph_3
    data_graph_3['time(seconds)'][interval] = x
    data_graph_3['cpu-1'][interval] = y

def update_data_graph_4(interval, x, y):
    global data_graph_4
    data_graph_4['time(seconds)'][interval] = x
    data_graph_4['cpu-2'][interval] = y

def update_data_graph_5(interval, x, y):
    global data_graph_5
    data_graph_5['time(seconds)'][interval] = x
    data_graph_5['cpu-3'][interval] = y

def update_data_graph_6(interval, x, y):
    global data_graph_6
    data_graph_6['time(seconds)'][interval] = x
    data_graph_6['cpu-4'][interval] = y

def update_data_graph_7(interval, x, y):
    global data_graph_7
    data_graph_7['time(seconds)'][interval] = x
    data_graph_7['cpu-5'][interval] = y

def update_data_graph_8(interval, x, y):
    global data_graph_8
    data_graph_8['time(seconds)'][interval] = x
    data_graph_8['cpu-6'][interval] = y

def update_data_graph_9(interval, x, y):
    global data_graph_9
    data_graph_9['time(seconds)'][interval] = x
    data_graph_9['cpu-7'][interval] = y

def update_data_graph_10(interval, x, y):
    global data_graph_10
    data_graph_10['time(seconds)'][interval] = x
    data_graph_10['cpu-8'][interval] = y

def update_data_graph_11(interval, x, y):
    global data_graph_11
    data_graph_11['time(seconds)'][interval] = x
    data_graph_11['cpu-9'][interval] = y

def update_data_graph_12(interval, x, y):
    global data_graph_12
    data_graph_12['time(seconds)'][interval] = x
    data_graph_12['cpu-10'][interval] = y

def update_data_graph_13(interval, x, y):
    global data_graph_13
    data_graph_13['time(seconds)'][interval] = x
    data_graph_13['cpu-11'][interval] = y

def update_data_graph_14(interval, x, y):
    global data_graph_14
    data_graph_14['time(seconds)'][interval] = x
    data_graph_14['cpu-12'][interval] = y

def update_data_graph_15(interval, x, y):
    global data_graph_15
    data_graph_15['time(seconds)'][interval] = x
    data_graph_15['cpu-13'][interval] = y

def update_data_graph_16(interval, x, y):
    global data_graph_16
    data_graph_16['time(seconds)'][interval] = x
    data_graph_16['cpu-14'][interval] = y

def update_data_graph_17(interval, x, y):
    global data_graph_17
    data_graph_17['time(seconds)'][interval] = x
    data_graph_17['cpu-15'][interval] = y


#################### GRAFICOS ####################

@callback(
    Output('traffic-graph', 'figure', ),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    if interval_graph_0 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_0(interval_graph_0, interval_graph_0 * 5, metrics_dict['traffic'])
        update_interval_graph_0()
        return {}
    else:
        dff = pd.DataFrame(data_graph_0)
        return px.line(dff, x='time(seconds)', y='traffic')

@callback(
    Output('memory-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_1(n):
    if interval_graph_1 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_1(interval_graph_1, interval_graph_1 * 5, metrics_dict['memory'])
        update_interval_graph_1()
        return {}
    else:
        dff = pd.DataFrame(data_graph_1)
        return px.line(dff, x='time(seconds)', y='memory')

@callback(
    Output('cpu-0-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_2(n):
    if interval_graph_2 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_2(interval_graph_2, interval_graph_2 * 5, metrics_dict['cpu-0'])
        update_interval_graph_2()
        return {}
    else:
        dff = pd.DataFrame(data_graph_2)
        return px.line(dff, x='time(seconds)', y='cpu-0')

@callback(
    Output('cpu-1-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_3(n):
    if interval_graph_3 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_3(interval_graph_3, interval_graph_3 * 5, metrics_dict['cpu-1'])
        update_interval_graph_3()
        return {}
    else:
        dff = pd.DataFrame(data_graph_3)
        return px.line(dff, x='time(seconds)', y='cpu-1')

@callback(
    Output('cpu-2-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_4(n):
    if interval_graph_4 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_4(interval_graph_4, interval_graph_4 * 5, metrics_dict['cpu-2'])
        update_interval_graph_4()
        return {}
    else:
        dff = pd.DataFrame(data_graph_4)
        return px.line(dff, x='time(seconds)', y='cpu-2')

@callback(
    Output('cpu-3-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_5(n):
    if interval_graph_5 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_5(interval_graph_5, interval_graph_5 * 5, metrics_dict['cpu-3'])
        update_interval_graph_5()
        return {}
    else:
        dff = pd.DataFrame(data_graph_5)
        return px.line(dff, x='time(seconds)', y='cpu-3')

@callback(
    Output('cpu-4-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_6(n):
    if interval_graph_6 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_6(interval_graph_6, interval_graph_6 * 5, metrics_dict['cpu-4'])
        update_interval_graph_6()
        return {}
    else:
        dff = pd.DataFrame(data_graph_6)
        return px.line(dff, x='time(seconds)', y='cpu-4')

@callback(
    Output('cpu-5-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_7(n):
    if interval_graph_7 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_7(interval_graph_7, interval_graph_7 * 5, metrics_dict['cpu-5'])
        update_interval_graph_7()
        return {}
    else:
        dff = pd.DataFrame(data_graph_7)
        return px.line(dff, x='time(seconds)', y='cpu-5')

@callback(
    Output('cpu-6-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_8(n):
    if interval_graph_8 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_8(interval_graph_8, interval_graph_8 * 5, metrics_dict['cpu-6'])
        update_interval_graph_8()
        return {}
    else:
        dff = pd.DataFrame(data_graph_8)
        return px.line(dff, x='time(seconds)', y='cpu-6')

@callback(
    Output('cpu-7-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_9(n):
    if interval_graph_9 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_9(interval_graph_9, interval_graph_9 * 5, metrics_dict['cpu-7'])
        update_interval_graph_9()
        return {}
    else:
        dff = pd.DataFrame(data_graph_9)
        return px.line(dff, x='time(seconds)', y='cpu-7')

@callback(
    Output('cpu-8-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_10(n):
    if interval_graph_10 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_10(interval_graph_10, interval_graph_10 * 5, metrics_dict['cpu-8'])
        update_interval_graph_10()
        return {}
    else:
        dff = pd.DataFrame(data_graph_10)
        return px.line(dff, x='time(seconds)', y='cpu-8')

@callback(
    Output('cpu-9-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_11(n):
    if interval_graph_11 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_11(interval_graph_11, interval_graph_11 * 5, metrics_dict['cpu-9'])
        update_interval_graph_11()
        return {}
    else:
        dff = pd.DataFrame(data_graph_11)
        return px.line(dff, x='time(seconds)', y='cpu-9')

@callback(
    Output('cpu-10-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_12(n):
    if interval_graph_12 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_12(interval_graph_12, interval_graph_12 * 5, metrics_dict['cpu-10'])
        update_interval_graph_12()
        return {}
    else:
        dff = pd.DataFrame(data_graph_12)
        return px.line(dff, x='time(seconds)', y='cpu-10')

@callback(
    Output('cpu-11-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_13(n):
    if interval_graph_13 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_13(interval_graph_13, interval_graph_13 * 5, metrics_dict['cpu-11'])
        update_interval_graph_13()
        return {}
    else:
        dff = pd.DataFrame(data_graph_13)
        return px.line(dff, x='time(seconds)', y='cpu-11')

@callback(
    Output('cpu-12-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_14(n):
    if interval_graph_14 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_14(interval_graph_14, interval_graph_14 * 5, metrics_dict['cpu-12'])
        update_interval_graph_14()
        return {}
    else:
        dff = pd.DataFrame(data_graph_14)
        return px.line(dff, x='time(seconds)', y='cpu-12')

@callback(
    Output('cpu-13-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_15(n):
    if interval_graph_15 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_15(interval_graph_15, interval_graph_15 * 5, metrics_dict['cpu-13'])
        update_interval_graph_15()
        return {}
    else:
        dff = pd.DataFrame(data_graph_15)
        return px.line(dff, x='time(seconds)', y='cpu-13')

@callback(
    Output('cpu-14-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_16(n):
    if interval_graph_16 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_16(interval_graph_16, interval_graph_16 * 5, metrics_dict['cpu-14'])
        update_interval_graph_16()
        return {}
    else:
        dff = pd.DataFrame(data_graph_16)
        return px.line(dff, x='time(seconds)', y='cpu-14')

@callback(
    Output('cpu-15-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_17(n):
    if interval_graph_17 < 10:
        metrics_dict = json.loads(redis_client.get('vitorferreira-proj3-output'))
        update_data_graph_17(interval_graph_17, interval_graph_17 * 5, metrics_dict['cpu-15'])
        update_interval_graph_17()
        return {}
    else:
        dff = pd.DataFrame(data_graph_17)
        return px.line(dff, x='time(seconds)', y='cpu-15')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=31216)