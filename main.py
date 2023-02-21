from fastapi import FastAPI
from requests import get

app = FastAPI()

API_KEY = 'E26BA322-3979-4B92-913B-E62A7AF5AB0B'
url = f"https://rest-sandbox.coinapi.io/v1/exchangerate/BTC/USD"
headers = {'X-CoinAPI-Key': API_KEY}

# res = get(url=url, headers=headers)
# print(res.json())


@app.get("/")
async def root():
    results = get(url=url, headers=headers)
    return dict(results.json())


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
