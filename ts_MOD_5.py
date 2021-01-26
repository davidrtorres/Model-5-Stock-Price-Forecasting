import pandas as pd

from datetime import datetime as dt, date

import dash
import plotly.express as px

from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime


app =dash.Dash(__name__)

app.layout = html.Div([
                        html.H1('Stock Price Information', style={'textAlign': 'center','color': 'blue'}),
                        #Enter Stock Symbol(s) separated by comma
                        html.Div([html.H3('Enter Stock Symbol(s)', style={'paddingRight':'20px','color': 'red'}),

                        dcc.Input(
                            id='my_ticker_symbol',
                            value='TSLA,AMZN',  #multi strings to get more than 1
                            style={'fontSize':24, 'width':75}
                        )], style={'display': 'inline-block','verticalAlign':'top'}), 

                        html.Div([html.H3('Select a Start and End Date',style={'color': 'red'}),
                                dcc.DatePickerRange(id='my_date_picker',
                                        min_date_allowed=datetime(2015,1,1),
                                        max_date_allowed=datetime.today(),
                                        start_date= datetime(2018,1,1),
                                        end_date = datetime.today()
                                                   )
                        ], style={'display':'inline-block'}),

                        html.Div([html.H3('Select Type of Data:', style={'paddingLeft':'20px','color': 'red'}),
                                dcc.Dropdown(
                                    id='mod_dropdown',
                                    options=[
                                        {'label': 'Adj Close', 'value': 'Adj Close'},
                                        {'label': 'Daily Price Change', 'value': 'Daily Price Change'}

                                    ],
                                    value='Adj Close',
                                    placeholder = "Select Type",
                                    
                                    style={'fontSize':18, 'marginLeft':'10px','color': 'red'},
                                ),
                                  
                            
                        ], style={'display':'inline-block','verticalAlign':'top'}), 
    
                        html.Div([
                                    html.Button(id='submit-button',
                                                n_clicks =0,
                                                children='Submit',
                                                style={'fontSize':24, 'marginLeft':'30px','color': 'red'})
                        ], style={'display':'inline-block'}),   
                            
                           

                        dcc.Graph(id='my_graph',
                                    figure={'data':[
                                                {'x':[1,2], 'y':[3,1]}  #{'x':[1,2], 'y':[3,1]}

                                    ], 'layout': {"title":'Default Title'}}

                        )

            ])
#title is updated based on what is inputed   
@app.callback(
Output('my_graph','figure'),
[Input('submit-button','n_clicks')],
[State('my_ticker_symbol','value'),
            State('my_date_picker', 'start_date'),
            State('my_date_picker', 'end_date'),
            State('mod_dropdown', 'value') 

        ])


#function that has decorator
def update_graph(n_clicks, stock, start_date,end_date, mod_dropdown): #for any name
        start = datetime.strptime(start_date[:10],'%Y-%m-%d')
        end= datetime.strptime(end_date[:10],'%Y-%m-%d')
            
        my_dict={}
        symbols = stock.split(',')  #value='TSLA,AMZN',
            
        for sym in symbols:
            try:
                my_dict[sym] = web.DataReader(sym,'yahoo',start_date,end_date)['Adj Close']
            except: #try except
                print("Can't locate symbol: " + sym)
        my_dict1 = pd.concat(my_dict, axis=1) 
            
        stocks_data = [s for s in my_dict1 if s in my_dict1.columns]
        if mod_dropdown == 'Adj Close':
            title="Adj Close Price Data"

            fig = px.line(my_dict1,x=my_dict1.index,y=stocks_data)
        else:
            fig = px.line(my_dict1.diff(),x=my_dict1.index,y=stocks_data)
            title="Daily Price Change  Data"    

        fig.update_layout(
                    title=title,
                    #xaxis_title="x Axis Title",
                    yaxis_title="Price USD ($)",
                    title_x=0.5,
                    font=dict(
                        family="Arial",
                        size=18,
                        color="black") )          
        return fig

# def run_server(self,
#                        port=8051,
#                        debug=True,
#                        threaded=True,
#                        **flask_run_options):
#             self.server.run(port=port, debug=debug, **flask_run_options)


#app.run_server(mode='inline',debug=True, port=8051)
server = app.server
if __name__ =='__main__':
    app.run_server(debug=True)

#CTRL + C to quit    