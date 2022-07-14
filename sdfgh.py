import datetime
import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = '''CREATE TABLE song (
                                artist,
                                name_song,
                                texst);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    # cursor.execute(sqlite_create_table_query)
    # sqlite_connection.commit()
    print("Таблица SQLite создана")
    cursor.execute("insert into sqlitedb_developers (id, name, email, joining_date, salary) values (?,?,?,?,?)",
                   (2,"qwe","65esm@mail.ru", datetime.datetime.now(), 23234234))
    sqlite_connection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

#finally:
 #   if (sqlite_connection):
   #     sqlite_connection.close()
  #      print("Соединение с SQLite закрыто")
