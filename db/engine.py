import sqlite3

def run_engine() -> None:
    try:
        # настройка подключения к таблице
        connection = sqlite3.connect("stalcraft.db")
        cursor = connection.cursor()

        # выполнение комманды
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS ItemHistoryLots 
               (id INTEGER PRIMARY KEY, price INTEGER, 
                amount INTEGER, time DATETIME)''')

        # подтверждение комманды
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
