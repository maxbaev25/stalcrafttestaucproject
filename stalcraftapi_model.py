import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os

from requests import Response


class Stalcraft:
    @staticmethod
    def get_item_price_history(
            item: str, region: str, token: str, order: str = None,
            sort: str = None, additional: bool = False,
            limit: int = 20, offset: int = 0,
            is_demo: bool = True) -> dict:
        if is_demo:
            version: str = "d"
        else:
            version: str = "e"
        url: str = f"https://{version}api.stalcraft.net/{region}/auction/{item}/history"
        response = Stalcraft.get_response_with_params(
            url, token, order, sort, additional, limit, offset)
        return response.json()

    @staticmethod
    def get_active_item_lots(
            item: str, region: str, token: str, order: str = None,
            sort: str = None, additional: bool = False,
            limit: int = 20, offset: int = 0,
            is_demo: bool = True) -> dict:
        if is_demo:
            version: str = "d"
        else:
            version: str = "e"
        url: str = f"https://{version}api.stalcraft.net/{region}/auction/{item}/lots"
        response = Stalcraft.get_response_with_params(
            url, token, order, sort, additional, limit, offset)
        return response.json()

    @staticmethod
    def get_response_with_params(
            url: str, token: str, order: str, sort: str,
            additional: bool, limit: int, offset: int) -> Response:
        response = requests.get(
            url=url, params=Stalcraft.set_params(order, sort, additional, limit, offset),
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json"})
        return response

    @staticmethod
    def get_response(
            url: str, token: str) -> Response:
        response = requests.get(
            url=url,
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json"})
        return response

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
        return params

    @staticmethod
    def get_regions(token: str,
                    is_demo: bool = True) -> list:
        if is_demo:
            version: str = "d"
        else:
            version: str = "e"
        url: str = f"https://{version}api.stalcraft.net/regions"
        response = Stalcraft.get_response(
            url, token)
        return response.json()


if __name__ == '__main__':
    load_dotenv()
    app_token = os.getenv("app_token")
    item_id = "4l7p"
    region = "ru"
    pp(Stalcraft.get_active_item_lots_demoapi(item_id, region, app_token, "asc", "buyout_price", True))
