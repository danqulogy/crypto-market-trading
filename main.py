from fastapi import FastAPI
from requests import get

from coinapi_service import CoinApiService

app = FastAPI()


@app.get("/")
async def root():
    service = CoinApiService()
    return service.get_exchange_rate('BTC', 'USD')


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
