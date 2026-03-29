import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os
from stalcraftapi_model import Stalcraft
from db import crud, engine
import asyncio

# envarement
load_dotenv()
app_token = os.getenv("token")
secret_token = os.getenv("secret_token")

# params
item_id = "4l7p"
region = "ru"

def get_history():
    history = Stalcraft.get_item_price_history(
        item=item_id, region=region, is_demo=True, token=app_token)
    for i in history['prices']:
        times = datetime.datetime.strptime(
            i['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        amount = i['amount']
        price = i['price']
        asyncio.run(crud.add_history_lot_async(
            amount=amount, time=times, price=price))


scheduler = BlockingScheduler()
scheduler.add_job(get_history, 'interval', seconds=5)
scheduler.start()
