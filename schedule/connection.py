import sqlite3
from sqlite3 import Error

def create_connection(db_file = "E:/Program/Python/Schedule/db_schedule.db"):
    #""" create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None