import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os

class Stalcraft:
    @staticmethod
    def get_item_price_history_demoapi(
            item: str, region: str, token: str, order: str = None, sort: str = None,
            additional: bool = False, limit: int = 20, offset: int = 0) -> dict:
        url: str = f"https://dapi.stalcraft.net/{region}/auction/{item}/history"
        response = requests.get(
            url=url, params=Stalcraft.set_params(order, sort, additional, limit, offset),
            headers={"Authorization": f"Bearer {token}"})
        return response.json()

    @staticmethod
    def get_active_item_lots_demoapi(
            item: str, region: str, token: str, order: str = None, sort: str = None,
            additional: bool = False, limit: int = 20, offset: int = 0):
        url: str = f"https://dapi.stalcraft.net/{region}/auction/{item}/lots"
        response = requests.get(
            url=url, params=Stalcraft.set_params(order, sort, additional, limit, offset),
            headers={"Authorization": f"Bearer {token}"})
        return response.json()

    @staticmethod
    def get_item_price_history_eapi(
            item: str, region: str, token: str, order: str = None, sort: str = None,
            additional: bool = False, limit: int = 20, offset: int = 0) -> dict:
        url: str = f"https://eapi.stalcraft.net/{region}/auction/{item}/history"
        response = requests.get(
            url=url, params=Stalcraft.set_params(order, sort, additional, limit, offset),
            headers={"Authorization": f"Bearer {token}"})
        return response.json()

    @staticmethod
    def get_active_item_lots_eapi(
            item: str, region: str, token: str, order: str = None, sort: str = None,
            additional: bool = False, limit: int = 20, offset: int = 0):
        url: str = f"https://eapi.stalcraft.net/{region}/auction/{item}/lots"
        response = requests.get(
            url=url, params=Stalcraft.set_params(order, sort, additional, limit, offset),
            headers={"Authorization": f"Bearer {token}"})
        return response.json()

    @staticmethod
    def set_params(order, sort ,additional, limit, offset) -> dict[str, str]:
        params = {"offset": f"{offset}", "limit": f"{limit}"}
        if order is not None:
            params["order"] = order
        if sort is not None:
            params["sort"] = sort
        if additional:
            params["additional"] = "true"
        else:
            params["additional"] = "false"
        pp(params)
        return params


if __name__ == '__main__':
    load_dotenv()
    app_token = os.getenv("app_token")
    item_id = "4l7p"
    region = "ru"
    pp(Stalcraft.get_active_item_lots_demoapi(item_id, region, app_token, "asc", "buyout_price", True))
