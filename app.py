import requests
from pprint import pprint, pp
from settings import app_token, user_token

item_id = "zzjgn"
response = requests.get(headers={"Authorization": app_token},
    url=f"https://dapi.stalcraft.net/ru/auction/{item_id}/history")

pp(response.json())
