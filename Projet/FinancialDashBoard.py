# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:02:03 2023

@author: alexm
"""
import dash                                # pip install dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import datetime
import base64

path = r"\\wsl.localhost\Ubuntu\home\alexandre\PrixBTC.csv"
df = pd.read_csv(path,sep=';')
    
def transform_date(date_string):                       
    #On ajoute une heure pour se ramener à l'heure francaise.
    date_obj = datetime.datetime.strptime(date_string, "%a %b %d %H:%M:%S %Z %Y") + pd.Timedelta(hours=1)
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
    return date_obj

def transform_nbr(nbr_string):
    formatted_nbr = nbr_string
    if type(nbr_string) == "str":
        formatted_nbr = float(nbr_string.replace("$","").replace(",", "").replace(".", ".")) 
    return formatted_nbr

# Appliquer la fonction à la colonne 
df['Date'] = df['Date'].apply(transform_date)
df['Prix'] = df['Prix'].apply(transform_nbr)
data = df




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

image_filename = 'C:/Users/alexm/Desktop/S8_Python/Asset/bitcoin-logo-font.jpg' # chemin vers votre image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

#app.layout = html.Div([
#    html.H1('Dashboard Prix du Bitcoin'),
#    dcc.Graph(id='graph'),
#])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                #html.Img(src='data:image/png;base64,{}'.format(encoded_image),style={"width": "6rem"}),
                dbc.CardBody([
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image),style={'textAlign': 'center','height':'100%',"width": "100%"}),
                        html.P("")
                        ,
                    
                        #html.P("Affichage 2")
                        html.Div(
                            [
                            html.H3('Informations sur les prix sur la journée'),
                            html.P("Nombre de lignes : {len(df)}"),
                            html.P("Prix minimum : {df['Prix'].min()} $"),
                            html.P("Prix maximum : {df['Prix'].max()} $"),
                            html.P("Variation du Prix : {round((df['Prix'][len(df)-1]-df['Prix'][0])/df['Prix'][0],2)} %"),
                            ],style={"textAlign": "center","width": "50%","margin": "auto"})
                        ,
                    
                        html.P("")
                        
                    ],style={'textAlign': 'center'})],
                style={"width": "24rem"}, className="mt-3")
            
            
            ]),
        dbc.Col([
            dbc.Card([
                    html.H1("Graphique des prix :"),
                    dcc.Checklist(
                        id='duration-checkbox',
                        options=[
                            {'label': '1 hour ', 'value': '1H'},
                            {'label': '20 min ', 'value': '4H'},
                            {'label': '1 day ', 'value': '1D'}
                        ],
                        value=['1H'],
                        style={'transform': 'scale(1.2)',"textAlign": "right"}
                    ),
                    dcc.Graph(
                    id='price-graph',
                    # figure={
                    #     'data': [
                    #         go.Scatter(
                    #             x=data['Date'],
                    #             y=data['Prix'],
                    #             mode='lines',
                    #             marker=dict(color='red'),
                    #             name='Prix'
                    #         )
                    #     ],
                    #     'layout': go.Layout(
                    #         title='Evolution des prix',
                    #         xaxis={'title': 'Date'},
                    #         yaxis={'title': 'Prix'}
                    #     )
                    # }
                )
            
            ])
            ])
        ]),
    dcc.Interval(id='update', n_intervals=0, interval=1000*5)
    ])


#fig = px.scatter(df, x=[1,2,3], y=[1,2,3])
@app.callback(Output('price-graph', 'figure'),
              Input('duration-checkbox', 'value'))
def update_price_graph(duration):
    if '1H' in duration:
        # afficher les données des dernières 1 heure
        data = df[df['Date'] >= pd.Timestamp('now') - pd.Timedelta(hours=1)]
    elif '4H' in duration:
        # afficher les données des dernières 4 heures
        data = df[df['Date'] >= pd.Timestamp('now') - pd.Timedelta(minutes=20)]
    elif '1D' in duration:
        # afficher les données des dernières 24 heures
        data = df[df['Date'] >= pd.Timestamp('now') - pd.Timedelta(days=5)]
    else:
        # afficher toutes les données
        data = df
    
    # Créez la figure pour le graphique de prix
    fig = {
        'data': [{'x': data['Date'], 'y': data['Prix'], 'type': 'line'}],
        'layout': {'title': 'Price over time'}
    }
    figure={   
        'data': [
            go.Scatter(
                x=data['Date'],
                y=data['Prix'],
                mode='lines',
                marker=dict(color='red'),
                name='Prix'
            )
        ],
        'layout': go.Layout(
            title='Évolution des prix',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Prix'}
        )
    }
    
    return figure

if __name__=='__main__':
    app.run_server(debug=True)
