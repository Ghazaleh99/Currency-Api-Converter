from decouple import config
from converter.models import Currency
import requests

key = config('API_KEY')
url = config('BASE_URL')

def culist():
    url1 = url+"list"
    payload = {}
    headers= {
        "apikey": key
    }
    response = requests.request("GET", url1, headers=headers, data = payload)
    data = response.json()
    symbols = data['currencies']
    return symbols

def exchangeRate():
    url1 = url+"live?"
    payload = {}
    headers= {
        "apikey": key
    }
    response = requests.request("GET", url1, headers=headers, data = payload)
    data = response.json()
    latest = data['quotes']
    return latest

def getlist():
    symbols = culist()
    exchange_rate = exchangeRate()
    for i in symbols:
        if Currency.objects.filter(symbol = i).exists():
            continue
        else:
            new = Currency(
                symbol = i,
                name = symbols[i],
            )
            if f'USD{i}' in exchange_rate:
                new.base = 'USD'
                new.bs_sym_rate = exchange_rate[f'USD{i}']
            new.save()

def scheduled_job():
    getlist()