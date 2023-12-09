from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
# print(df[df.country=='Canada'].to_dict())
# print(df[df.country=='Canada'])

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='graph-content', style={'textAlign':'center'}),
    dcc.Graph(id='graph-content'),
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

data_graph_0 = {'year': {}, 'pop': {}}
data_graph_1 = {'year': {}, 'pop': {}}
data_graph_2 = {'year': {}, 'pop': {}}

def update_data_graph_0(interval, x, y):
    global data_graph_0
    data_graph_0['year'][interval] = x
    data_graph_0['pop'][interval] = y

@callback(
    Output('graph-content', 'figure', ),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    #print("intervals from graph 0: " + str(interval_graph_0))

    dff = pd.DataFrame({'instante da medicao': {0: 1980, 1: 1981, 2: 1982, 3: 1983, 4: 1984, 5: 1985, 6: 1986, 7: 1987, 8: 1988, 9: 1989}, 'porcentagem trafico outgoing': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}})
    return px.line(dff, x='instante da medicao', y='porcentagem trafico outgoing')
    
    # if interval_graph_0 < 10:
    #     print("Still gathering data 0: " + str(data_graph_0))
    #     update_data_graph_0(interval_graph_0, 1980, 5)
    #     update_interval_graph_0()
    #     return {}
    # else:
    #     dff = pd.DataFrame(data_graph_0)
    #     print(dff)
    #     return px.line(dff, x='year', y='pop')


    # redis_dict = {"cpu-0": 4.999999999999999, "cpu-1": 4.375, "cpu-2": 4.2749999999999995, "cpu-3": 31.900000000000002, "cpu-4": 4.866666666666666, "cpu-5": 3.65, "cpu-6": 7.291666666666665, "cpu-7": 5.649999999999999, "cpu-8": 8.608333333333334, "cpu-9": 5.358333333333334, "cpu-10": 4.249999999999999, "cpu-11": 5.008333333333334, "cpu-12": 4.041666666666667, "cpu-13": 6.300000000000001, "cpu-14": 17.458333333333332, "cpu-15": 3.899999999999999, "traffic": 0.022827359293588544, "memory": 0.507892948192654}
    # redis_dict_in_dataframe_form = pd.
    # dff = df[df.country=='Canada']
    # return px.line(dff, x='year', y='pop')

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