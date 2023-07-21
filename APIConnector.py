import requests

class APIConnector:
    def __init__(self, APIKey):
        self.__APIKey = APIKey
        
    
    def getCurrencyCodesAndNames(self):
        return requests.get('https://api.currencyfreaks.com/v2.0/currency-symbols')