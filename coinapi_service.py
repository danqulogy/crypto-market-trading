from json import loads, dumps

from requests import get


class CoinApiService:
    API_KEY = 'E26BA322-3979-4B92-913B-E62A7AF5AB0B'
    headers = {'X-CoinAPI-Key': API_KEY}

    async def get_exchanges(self) -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchanges"
        results = get(url=url, headers=self.headers)
        print(results.json())
        return dict(results.json())

    def get_single_exchange(self, exchange_id: str = 'BTC') -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchanges/{exchange_id}"
        params = {
            "filter_exchange_id": []
        }

        results = get(url=url, headers=self.headers, params=params)
        return dict(results.json())

    def get_exchange_rate(self, baseCurrency: str = 'BTC', quoteCurrency: str = 'USD') -> dict:
        url = f"https://rest-sandbox.coinapi.io/v1/exchangerate/{baseCurrency}/{quoteCurrency}"
        results = get(url=url, headers=self.headers)
        return dict(results.json())

    def make_api_call(url:str, headers, params):
        # Making GET request
        res = get(url=url, headers=headers, params=params)

        # Checking if API returns any errors in the response
        if res.status_code != 200:
            # Printing custom status error message
            print(res)
            return

        # Printing custom header elements header element
        print(res.headers)

        # Printing a clean JSON response
        print("\nJSON Response:")
        parsed_json = loads(res.content)
        formatted_json = dumps(parsed_json, indent=4)
        print(formatted_json)