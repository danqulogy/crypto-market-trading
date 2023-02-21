from fastapi import FastAPI
from requests import get

from coinapi_service import CoinApiService

app = FastAPI()


@app.get("/")
async def get_exchange_rate(base_asset: str, quote_asset: str):
    service = CoinApiService()
    return service.get_exchange_rate(base_asset, quote_asset)


@app.get("/exchanges")
async def get_exchanges():
    service = CoinApiService()
    return service.get_exchanges()


@app.get("/exchanges/{exchange_id}")
async def get_single_exchange(exchange_id: str):
    service = CoinApiService()
    return service.get_single_exchange(exchange_id)


@app.get("/exchanges/icons")
async def get_exchange_icons():
    service = CoinApiService()
    return service.get_exchange_icons()


@app.get("/assets")
async def get_assets():
    service = CoinApiService()
    return service.get_assets()


@app.get("/assets/{asset_id}")
async def get_single_asset(asset_id: str):
    service = CoinApiService()
    return service.get_single_asset(asset_id)


@app.get("/assets/icons")
async def get_asset_icons():
    service = CoinApiService()
    return service.get_exchange_icons()
