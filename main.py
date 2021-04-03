import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import pickle
import threading as Threading
from data_submodule import get_data

# Create a thread for "getting data" in these python files the data is actually created instead of retrieved,
# from somewhere else but i call the function get_data because in real life you want to probably get data from
# a sensor, csv file, sql table or whatever. This is the moment where the old code could get you into trouble...
# Btw for a tutorial about threading see https://www.youtube.com/watch?v=IEEhzQoKtQU&t=493s
t1 = Threading.Thread(target=get_data)
t1.start()

# Unchanged dash app layout
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

# New adjusted callback
@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_scatter(input_data):
    # get the data from a pickle file
    data_X_Y = pickle.load(open("data_X_Y.p", "rb"))
    print(data_X_Y)
    X = data_X_Y[0]
    Y = data_X_Y[1]
    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080 ,debug=True)
