import json
import requests
from config import ACCESS_KEY, valuty

class APIException(Exception):
    pass
class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException ('Введены одинаковые обозначения валюты')
        try:
            quote_ticker = valuty[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = valuty[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')


        r = requests.get(f'https://v6.exchangerate-api.com/v6/{ACCESS_KEY}/pair/{base_ticker}/{quote_ticker}')
        total_base = json.loads(r.content)['conversion_rate']
        return total_base * amount






