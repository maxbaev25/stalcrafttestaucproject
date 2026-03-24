from datetime import datetime
import sqlite3

def add_history_lot(
        amount: int, time: datetime, price: int) -> None:
    try:
        connection = sqlite3.connect("stalcraft.db")
        cursor = connection.cursor()
        cursor.execute(
            f'''INSERT INTO ItemHistoryLots 
                   (price, amount, time) 
               VALUES ({price}, {amount}, '{time}')'''
        )
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
