from sqlite3 import connect
import sqlite3


def table_user():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Create Table If Not Exists users (
    id Integer Primary Key Unique,
    telegram_id Integer,
    first_name Varchar(150)
    )   
    """)
    conn.commit()
table_user()

def save_users(telegram_id,first_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into users (telegram_id,first_name)
    Values({telegram_id},"{first_name}")
    """)
    conn.commit()


def get_user_id(telegram_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Select * from users
    where telegram_id = {telegram_id}
    """)
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False

def count_users():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from users
    """)
    data = cursor.fetchall()
    return data