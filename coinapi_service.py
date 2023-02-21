from requests import get


class CoinApiService:
    API_KEY = 'E26BA322-3979-4B92-913B-E62A7AF5AB0B'
    headers = {'X-CoinAPI-Key': API_KEY}

    def get_exchange_rate(self, baseCurrency: str = 'BTC', quoteCurrency: str = 'USD') -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchangerate/{baseCurrency}/{quoteCurrency}"
        results = get(url=url, headers=self.headers)
        return dict(results.json())