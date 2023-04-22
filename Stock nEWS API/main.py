"""THE CODE IS NOT WORKING DUE TO THE API ERROR . Sorry!!!!! """





STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY="P7FEEGDXXECOBSTM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
import os
import json
import datetime

parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "interval":"60min",
    "apikey":API_KEY,
}

now=datetime.datetime.today()
# print(now.split(' ')[0])
responses=requests.get(url=STOCK_ENDPOINT,params=parameters)
responses.raise_for_status()
data=responses.json()
print(data)
