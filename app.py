import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os

from sqlalchemy import null

from stalcraftapi_model import Stalcraft
from db import crud, engine
import asyncio
from tkinter import ttk
import tkinter



# envarement
load_dotenv()
app_token = os.getenv("token")
secret_token = os.getenv("secret_token")
my_root = tkinter.Tk()
my_root.title("REGION")
region=""

def confirm():
    global region
    region = combo_box.get()
    my_root.destroy()


selected = tkinter.StringVar()
all_regions = Stalcraft.get_regions(app_token)
regions_id = []
for reg in all_regions:
    regions_id.append(reg["id"])
combo_box = ttk.Combobox(my_root, values=regions_id, textvariable=selected)
combo_box.set("Выбери регион")
combo_box.pack()
tkinter.Button(my_root, text="Подтвердить", command=confirm).pack()
my_root.mainloop()

# params

item_id = "4l7p"
region = ""

def get_history():
    history = Stalcraft.get_item_price_history(
        item=item_id, region=region, is_demo=True, token=app_token)
    for i in history['prices']:
        times = datetime.datetime.strptime(
            i['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        amount = i['amount']
        price = i['price']
        asyncio.run(crud.add_history_lot_async(
            amount=amount, time=times, price=price,
            region=region, item=item_id))





scheduler = BlockingScheduler()
scheduler.add_job(get_history, 'interval', seconds=5)
scheduler.start()
