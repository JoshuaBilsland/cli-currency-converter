import requests

class APIConnector:
    def __init__(self, APIKey):
        self.__APIKey = APIKey
        
    
    def getCurrencyCodesAndNames(self):
        return requests.get(f'https://v6.exchangerate-api.com/v6/{self.__APIKey}/codes')
    
    
    def makeConversion(self, fromCurrency, toCurrency, amount):
        return requests.get(f"https://v6.exchangerate-api.com/v6/{self.__APIKey}/pair/{fromCurrency}/{toCurrency}/{amount}")