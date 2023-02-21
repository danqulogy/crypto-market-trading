from json import loads, dumps
from typing import List

from requests import get

from base_http_service import BaseHttpService


class CoinApiService(BaseHttpService):
    API_KEY = 'E26BA322-3979-4B92-913B-E62A7AF5AB0B'
    headers = {'X-CoinAPI-Key': API_KEY}

    def get_exchange_icons(self, icon_size: int = 12) -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchanges/icons{icon_size}"
        return self.get(url=url, headers=self.headers)

    def get_exchanges(self, allowed_exchanges=None) -> List[dict]:
        if allowed_exchanges is None:
            allowed_exchanges = []
        url = f"https://rest-sandbox.coinapi.io/v1/exchanges"
        params = {
            "filter_exchange_id": allowed_exchanges
        }
        return self.get(url, headers=self.headers, params=params)

    def get_single_exchange(self, exchange_id: str = 'BTC') -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchanges/{exchange_id}"
        return self.get(url=url, headers=self.headers)

    def get_exchange_rate(self, baseCurrency: str = 'BTC', quoteCurrency: str = 'USD') -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchangerate/{baseCurrency}/{quoteCurrency}"
        results = get(url=url, headers=self.headers)
        return dict(results.json())
