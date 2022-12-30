import sqlite3

import pandas as pd


def insert_pupil(data: tuple) -> None:
    backup()
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        name, number, telegram_id = data
        sqlite_insert_query = """INSERT INTO pupils (name, number, telegram_id) VALUES  (?, ?, ?);"""

        cursor.execute(sqlite_insert_query, (name, number, telegram_id))
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert_answer(day: str, answer: str, tg_id: int, date: str) -> None:
    backup()
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        
        if day == 'dayfirst':
            sqlite_insert_query = f"""UPDATE pupils SET dayfirst=?, day1date=? WHERE telegram_id=?;"""
        if day == 'daysecond':
            sqlite_insert_query = f"""UPDATE pupils SET daysecond=?, day2date=? WHERE telegram_id=?;"""
        if day == 'daythird':
            sqlite_insert_query = f"""UPDATE pupils SET daythird=?, day3date=? WHERE telegram_id=?;"""
        if day == 'dayfourth':
            sqlite_insert_query = f"""UPDATE pupils SET dayfourth=?, day4date=? WHERE telegram_id=?;"""
        if day == 'dayfifth':
            sqlite_insert_query = f"""UPDATE pupils SET dayfifth=?, day5date=? WHERE telegram_id=?;"""
        if day == 'daysixth':
            sqlite_insert_query = f"""UPDATE pupils SET daysixth=?, day6date=? WHERE telegram_id=?;"""
        if day == 'dayseventh':
            sqlite_insert_query = f"""UPDATE pupils SET dayseventh=?, day7date=? WHERE telegram_id=?;"""
        if day == 'dayeighth':
            sqlite_insert_query = f"""UPDATE pupils SET dayeighth=?, day8date=? WHERE telegram_id=?;"""

        cursor.execute(sqlite_insert_query, (answer, date, tg_id))
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def select_pupils_name(tg_id: int) -> None:
    try:
        sqlite_connection= sqlite3.connect('sqlite_python.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT name from pupils WHERE telegram_id=?;"""
        cursor.execute(sqlite_select_query, (tg_id,))
        name = cursor.fetchone()
        name = name[0]
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return name


def check_user(tg_id: int):
    try:
        sqlite_connection= sqlite3.connect('home/TechnoBot/data/sqlite_python.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from pupils WHERE telegram_id=?;"""
        cursor.execute(sqlite_select_query, (tg_id,))
        user = cursor.fetchone()
        print(user)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            
    if user is None:
        return False

    if tg_id in user:
        return True

def answer_is_none(tg_id: int, day: str):
    try:
        sqlite_connection= sqlite3.connect('sqlite_python.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = f"""SELECT {day} from pupils WHERE telegram_id=?;"""
        cursor.execute(sqlite_select_query, (tg_id,))
        answer = cursor.fetchone()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    print(answer)
    if None in answer:
        return True
    return False



def backup():
    def progress(status, remaining, total):
        print(f'Скопировано {total-remaining} из {total}...')

    try:
        sqlite_con = sqlite3.connect('sqlite_python.db')
        backup_con = sqlite3.connect('sqlite_backup.db')
        with backup_con:
            sqlite_con.backup(backup_con, pages=3, progress=progress)
        print("Резервное копирование выполнено успешно")
    except sqlite3.Error as error:
        print("Ошибка при резервном копировании: ", error)
    finally:
        if(backup_con):
            backup_con.close()
            sqlite_con.close()

def take_all_info():
    try:
        sqlite_connection= sqlite3.connect('sqlite_python.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = f"""SELECT * from pupils;"""
        cursor.execute(sqlite_select_query)
        
        df = pd.read_sql(sqlite_select_query, sqlite_connection)
        print(df)
        df.to_excel("data/from_bot/data.xlsx")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# create_db()
# create_table()
# insert_pupil(('Dorofeev Matvey Alexandrovich', '89659594943', 1123456789))
# name = select_pupils_name(1123456789)
# print(name*100)
# print(not check_user(1123345353))
# insert_answer('dayfirst', 'test', 1123456789, '30.12.2022')
