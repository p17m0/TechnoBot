import sqlite3

def create_db() -> None:
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def create_table() -> None:
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        sqlite_create_table_query = '''CREATE TABLE pupils (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    number TEXT NOT NULL UNIQUE,
                                    telegram_id INTEGER NOT NULL UNIQUE,
                                    dayfirst TEXT,
                                    day1date TEXT,
                                    daysecond TEXT,
                                    day2date TEXT,
                                    daythird TEXT,
                                    day3date TEXT,
                                    dayfourth TEXT,
                                    day4date TEXT,
                                    dayfifth TEXT,
                                    day5date TEXT,
                                    daysixth TEXT,
                                    day6date TEXT,
                                    dayseventh TEXT,
                                    day7date TEXT,
                                    dayeighth TEXT,
                                    day8date TEXT);'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")