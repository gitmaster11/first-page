from sqlite3 import connect
import sqlite3

def users():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute("""
    Create Table If Not Exists users (
    id Integer Primary Key Unique,
    ish_joyi Text,
    telegram_id Integer,
    age Integer,
    xodim Text,
    degree Text,
    job_type Text,
    vazifasi Text,
    ish_vaqti Text,
    salary Text,
    manzil Text,
    adding Text,
    phone Integer,
    name Text,
    view Integer
    )   
    """)
    conn.commit()
users()

def insert_table(ish_joyi,telegram_id,age,xodim,degree,ish_turi,vazifasi,ish_vaqti,salary,manzil,adding,phone,name,view):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into users(ish_joyi,telegram_id,age,xodim,degree,job_type,vazifasi,ish_vaqti,salary,manzil,adding,phone,name,view)
    values ("{ish_joyi}","{telegram_id}","{age}","{xodim}","{degree}","{ish_turi}","{vazifasi}","{ish_vaqti}","{salary}","{manzil}","{adding}","{phone}","{name}","{view}")
    """)
    conn.commit()

def get_area_from_db(ish_joyi):
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from users
    where ish_joyi = "{ish_joyi}"
    """)
    data = cursor.fetchall()
    return data
def adding_view(area):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Update users
    Set  view = view+1
    where ish_joyi = "{area}"
    """)
    conn.commit()
    
def for_using_users():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute("""
    Create Table If Not Exists for_using (
    id Integer Primary Key Unique,
    telegram_id Integer,
    name Text)
    """)
    conn.commit()
for_using_users()

def insert_table_for_using(tg_id,name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into for_using(telegram_id,name)
    values ("{tg_id}","{name}")
    """)
    conn.commit()


def getting_for_using(tg_id):
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from for_using
    where telegram_id = "{tg_id}"
    """)
    data = cursor.fetchall()
    return data

def getting_users():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from for_using
    """)
    data = cursor.fetchall()
    return data

    
def staff_table():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute("""
    Create Table If Not Exists staff (
    id Integer Primary Key Unique,
    name Text,
    area Text,
    telegram_id Integer
    )   
    """)
    conn.commit()
staff_table()

def insert_staff(name,area,tg_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into staff(name,area,telegram_id)
    values ("{name}","{area}","{tg_id}")
    """)
    conn.commit()


def get_staff(tg_id):
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from staff
    where telegram_id = "{tg_id}"
    """)
    data = cursor.fetchall()
    return data

def update_area(id,area):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Update staff
    Set  area = "{area}"
    where telegram_id = "{id}"
    """)
    conn.commit()


def get_send_staff(area):
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from staff
    where area = "{area}"
    """)
    data = cursor.fetchall()
    return data


def table_for_staff():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute("""
    Create Table If Not Exists table_for_staff (
    id Integer Primary Key Unique,
    telegram_id Integer
    )   
    """)
    conn.commit()
table_for_staff()

def insert_table_for_staff(telegram_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into table_for_staff(telegram_id)
    values ("{telegram_id}")
    """)
    conn.commit()

def get_table_for_staff():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from table_for_staff
    """)
    data = cursor.fetchall()
    return data

def check_user_in_tableforstaff(id):
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from table_for_staff
    where telegram_id = "{id}"
    """)
    data = cursor.fetchall()
    return data
