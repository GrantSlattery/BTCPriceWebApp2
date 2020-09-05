#Grant Slattery
#9/4/20
#Source of project: https://dash.plotly.com/datatable
#API & data Powered by CoinDesk: https://www.coindesk.com/price/bitcoin
#Scraping data and displaying it on the web using dash, 
#panda, requests, and more with Python
#This is part two: Reorganized and filtered data while adding style

import dash
import dash_table
import pandas as pd
import requests
import numpy as np


#############
#Scrape data#
#############

#Scraping with requests
bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
#Addition work for requests
response = requests.get(bitcoin_api_url)
response_json = response.json()


#################
#Refine raw data#
#################

#First round of raw data cleaning
priceData = response_json.get("bpi")


#Create Dash Table Data Frame with priceData variable
newpdFrame = pd.DataFrame(data=priceData)


#########################
#Display data on the web#
#########################

app = dash.Dash(__name__)
app.layout = dash_table.DataTable(
    id='table',
    columns = [{"name": i, "id": i} for i in newpdFrame.index],
    data = list((newpdFrame.to_dict()).values()), 
    
    #Add more style to the table
    style_as_list_view=True,  
    style_header={'backgroundColor': 'rgb(30, 30, 30)',
    'fontWeight': 'bold',
    'border': '2px solid green'
    },
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'textAlign': 'center',
        'padding': '10px',
    },
    style_data={ 'border': '2px solid green' },
    #Filter unusable raw data
    style_header_conditional=[
        {
        'if': {
               'column_id': 'symbol',
            },
            'display': 'none',
        },
        {
            'if': {
                'column_id': 'rate_float',
            },
            'display': 'none',
        },
    ],
    style_data_conditional=[
        {
            'if': {
               'column_id': 'symbol',
            },
            'display': 'none',
        },
        {
            'if': {
                'column_id': 'rate_float',
            },
            'display': 'none',
        },
    ]   
)

print("Program running")

if __name__ == '__main__':
    app.run_server(debug=True)