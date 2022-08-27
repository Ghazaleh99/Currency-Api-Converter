from decouple import config
from converter.models import Currency
import requests
from django.core.management.base import BaseCommand, CommandError

def handleRequests(r):
    if r.status_code == 429:
        print("too many requests")
        return False
    elif r.status_code == 401:
        print("No valid API key provided.")
        return False
    return True

class Command(BaseCommand):
    help = 'The help information for cron command.'
    key = config('API_KEY')
    url = config('BASE_URL')
    # def add_arguments(self, parser):
    #     parser.add_argument('MyCron', type=str, help='cron')
    
    def culist(self):
        url1 = self.url+"list"
        payload = {}
        headers= {
            "apikey": self.key
        }
        response = requests.request("GET", url1, headers=headers, data = payload)
        if handleRequests(response):
            data = response.json()
            symbols = data['currencies']
            return symbols
        return 0
        
    def exchangeRate(self):
        url1 = self.url+"live?"
        payload = {}
        headers= {
            "apikey": self.key
        }
        response = requests.request("GET", url1, headers=headers, data = payload)
        if handleRequests(response):
            data = response.json()
            latest = data['quotes']
            return latest
        return 0

    def handle(self, *args, **kwargs):
        # Currency.objects.all().delete()
        symbols = self.culist()
        exchange_rate = self.exchangeRate()
        if symbols == 0 or exchange_rate == 0:
            return
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

