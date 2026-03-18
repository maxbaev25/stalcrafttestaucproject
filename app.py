import time

import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os
from stalcraftapi_model import Stalcraft

# env
load_dotenv()
app_token = os.getenv("app_token")
secret_token = os.getenv("secret_token")

# vars
item_id = "4l7p"
region = "ru"

# response
while True:
    pp(Stalcraft.get_item_price_history(item_id, region, app_token))
    time.sleep(10)
