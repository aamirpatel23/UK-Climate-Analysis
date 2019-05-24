import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash(__name__)

paper={'0':['WGWP1.csv','WGWP2.csv','WGWP3.csv','WGWP4.csv','WGWP5.csv','WGWP6.csv','WGWP7.csv','WGWP8.csv','WGWP9.csv'],
       '1':['SGW1.csv','SGW2.csv','SGW3.csv','SGW4.csv','SGW5.csv','SGW6.csv','SGW7.csv','SGW8.csv','SGW9.csv'],
       '2':['ASDI1.csv','ASDI2.csv','ASDI3.csv','ASDI4.csv','ASDI5.csv','ASDI6.csv','ASDI7.csv','ASDI8.csv','ASDI9.csv'],
       '3':['SGD1.csv','SGD2.csv','SGD3.csv','SGD4.csv','SGD5.csv','SGD6.csv','SGD7.csv','SGD8.csv','SGD9.csv'],
       '4':['ASD1.csv','ASD2.csv','ASD3.csv','ASD4.csv','ASD5.csv','ASD6.csv','ASD7.csv','ASD8.csv','ASD9.csv']
      }
title={'0':['Daily Rainfall in UK(1910-2016)','Daily Max Temperature of UK (1960 - 2016)','Rainfall above 10 mm in a day(1960-2016)','Rainfall above 10 mm in a day(1960-2016)',
            'Training from 1960 to 2000 Testing from 2000 to 2016','Training from 1960 to 2016 Testing from 2000 to 2016','Forecast for rainfall in winter'],
       '1':['Daily Max Temperature of UK (1960 - 2016)','Daily Rainfall in UK(1910-2016)','Daily Max Temperature of UK (1960 - 2016)','Temperature above 18 Degree (1960 - 2016)',
            'Training from 1960 to 2009, Testing from 2010 to 2016','Training from 1960 to 2009, Testing from 2010 to 2016','Forecast for Temperature in Summer'],
       '2':['Monthly Sunshine in UK(1929-2016)','Monthly Sunshine in UK (1929 - 2016)','Total number of Hours of Sunshine in a Year (1929 - 2016)','Total number of Hours of Sunshine in a Year (1929 - 2016)',
            'Training from 1929 to 2006, Testing from 2006 to 2016','Training from 1929 to 2016, Testing from 2006 to 2016','Forecast for total number of hours of sunshine in a year'],
       '3':['Daily Rainfall in UK (1910 - 2016)','Daily Rainfall in the UK (1910 - 2016)','Rainfall below 1 mm in a day (1960 - 2016)','Rainfall below 1 mm in a day (1960 - 2016)',
           'Training from 1960 to 2009, Testing from 2010 to 2016','Training from 1960 to 2016, Testing from 2010 to 2016','Number of Days having rainfall < 1 mm during Summer'],
       '4':['Monthly Snowfall in UK (1971 - 2011)','Monthly Snowfall in UK (1971 - 2011)','Snowfall more than 5 days in a winter season (1971 - 2011)','Snowfall more than 5 days in a winter season (1971 - 2011)',
            'Training from 1971 to 2005, Testing from 2005 to 2011','Training from 1971 to 2011, Testing from 2005 to 2011','Forecast for total number of hours of sunshine in a year from 2017']
      }

app.layout = html.Div([
    html.H1( children='UK Climate Change', style={ 'textAlign': 'center', 'color': 'black' } ),

    html.Div([
        dcc.Dropdown(
            id='dropdown1',
            options=[{'label': 'WinterGettingWetter', 'value': '0'},
                     {'label': 'SummerGettingWarmer', 'value': '1'},
                     {'label': 'AnnualSunshineDurationIncreases', 'value': '2'},
                     {'label': 'SummerGettingDrier', 'value': '3'},
                     {'label': 'AnnualSnowfallDecreases', 'value': '4'}],
            value='0'
        )
    ],style={'width': '20%', 'display': 'inline-block', 'align': 'left', 'margin-left': '30%', 'margin-top': '5%'}),

    html.Div([
        dcc.Dropdown(
            id='dropdown2',
            options=[{'label': 'Data Plot', 'value': '0'},
                     {'label': 'Best Fit 1', 'value': '1'},
                     {'label': 'line 1', 'value': '2'},
                     {'label': 'Best Fit 2', 'value': '3'},
                     {'label': 'Forecast without check', 'value': '4'},
                     {'label': 'Forecast with check', 'value': '5'},
                     {'label': 'Final', 'value': '6'},
                    ],
            value='0'
        )
    ],style={'width': '20%', 'display': 'inline-block', 'align': 'right', 'margin-right': '20%'}),
        
    dcc.Graph(id='graph'),   
])
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [
        dash.dependencies.Input('dropdown1', 'value'),
        dash.dependencies.Input('dropdown2', 'value')
    ]
)
def update_figure(dropdown1,dropdown2):
    if dropdown2=='0':
        df1=pd.read_csv(paper[dropdown1][0])
        Data={
            "x": df1['Year'], 
            "y": df1['Data'], 
            "name": "DailyMean",   
        }
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][0]
                }),   
            'data': [Data],            
        }
    if dropdown2=='1':
        df1=pd.read_csv(paper[dropdown1][0])
        df2=pd.read_csv(paper[dropdown1][1])
        Data=go.Scatter(
            x= df1['Year'], 
            y= df1['Data'], 
            mode= "markers", 
            marker= {"color": "red"}, 
            name= "Data", 
        )
        FitLine=go.Scatter(
            x= df2['Year'], 
            y= df2['Data'], 
            line = dict(
                color = ('blue')
            ),
            name = ('FitLine')
        )
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][1]
                }),   
            'data': [Data,FitLine],            
        }
    if dropdown2=='2':
        df1=pd.read_csv(paper[dropdown1][2])
        Data={
            "x": df1['Year'], 
            "y": df1['Data'], 
            "name": "Data",   
        }
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][2]
                }),   
            'data': [Data],            
        }
    if dropdown2=='3':
        df1=pd.read_csv(paper[dropdown1][2])
        df2=pd.read_csv(paper[dropdown1][3])
        Data=go.Scatter(
            x= df1['Year'], 
            y= df1['Data'], 
            mode= "markers", 
            marker= {"color": "red"}, 
            name = ('Data')
        )
        FitLine=go.Scatter(
            x= df2['Year'], 
            y= df2['Data'], 
            line = dict(
                color = ('blue')
            ),
            name = ('FitLine')
        )
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][3]
                }),   
            'data': [Data,FitLine],            
        }
    if dropdown2=='4':
        df1=pd.read_csv(paper[dropdown1][4])
        df2=pd.read_csv(paper[dropdown1][5])
        Observe=go.Scatter(
            x= df1['Year'], 
            y= df1['Data'], 
            line = dict(
                color = ('blue')
            )  ,
            name = ('Observe')
        )
        Forecast=go.Scatter(
            x= df2['Year'], 
            y= df2['Data'], 
            line = dict(
                color = ('orange')
            ) ,
            name = ('Forecast')
        )
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][4]
                }),   
            'data': [Observe,Forecast],            
        }
    if dropdown2=='5':
        df1=pd.read_csv(paper[dropdown1][6])
        df2=pd.read_csv(paper[dropdown1][5])
        Observe=go.Scatter(
            x= df1['Year'], 
            y= df1['Data'], 
            line = dict(
                color = ('blue')
            ) ,
            name = ('Observe')
        )
        Forecast=go.Scatter(
            x= df2['Year'], 
            y= df2['Data'], 
            line = dict(
                color = ('orange')
            ),
            name = ('Forecast')
        )
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][5]
                }),   
            'data': [Observe,Forecast],            
        }
    if dropdown2=='6':
        df1=pd.read_csv(paper[dropdown1][7])
        df2=pd.read_csv(paper[dropdown1][8])
        Observe=go.Scatter(
            x= df1['Year'], 
            y= df1['Data'], 
            line = dict(
                color = ('blue'), 
            ) ,
            name = ('Observe')
        )
        Forecast=go.Scatter(
            x= df2['Year'], 
            y= df2['Data'], 
            line = dict(
                color = ('orange')
            ),
            name = ('Forecast')
        )
        return{
            'layout': go.Layout(
                xaxis={
                    'title': title[dropdown1][6]
                }),   
            'data': [Observe,Forecast],            
        }
if __name__ == '__main__':
    app.run_server(debug=True)