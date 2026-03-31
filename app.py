import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os
from stalcraftapi_model import Stalcraft
from db import crud
import sys

# envarement
load_dotenv()
app_token = os.getenv("token")
secret_token = os.getenv("secret_token")

# vars
item_id = "4l7p"
region = input("Input region: ")
regions = Stalcraft.get_regions(app_token, is_demo=True)
is_correct_region = True
for reg in regions:
    if reg["id"] != region or reg["name"] != region:
        is_correct_region = False
    else:
        is_correct_region = True
if not is_correct_region:
    sys.exit("Ошибка, регион не существует")

def get_history():
    history = Stalcraft.get_item_price_history(
        item=item_id, region=region, is_demo=True, token=app_token)
    for i in history['prices']:
        times = datetime.datetime.strptime(
            i['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        amount = i['amount']
        price = i['price']
        crud.add_history_lot(
            amount=amount, time=times, price=price)


scheduler = BlockingScheduler()
scheduler.add_job(get_history, 'interval', seconds=5)
scheduler.start()
