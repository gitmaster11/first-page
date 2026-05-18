from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from database import *


def phone_button():
    button = [      
        [KeyboardButton('Share to contact',request_contact = True)] 
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,one_time_keyboard = True)
def join_channel():
    button=  [
        [InlineKeyboardButton("Join Channel 🔜",url = 'https://t.me/sariqdevchat')],
        [InlineKeyboardButton("Tekshirish 🔎",callback_data = 'check_channel')]
    ]
    return InlineKeyboardMarkup(button)


def button_books():
    data = books_category_select()
    button  = []
    res = []
    for i in data:
        res.append(InlineKeyboardButton(i[1], callback_data = i[0]))
        if len(res)==2:
            button.append(res)
            res = []
    if len(res)>0:
        button.append(res)
    res = []
    button.append([InlineKeyboardButton("Kitob Savatchangiz 🛒 ", callback_data = 'self_books')])
    button.append([InlineKeyboardButton("Buyurtmalar tarixi 📜 ",callback_data ='history')])
    
    res.append(InlineKeyboardButton("Admin Panel ",callback_data = 'admin'))
    res.append(InlineKeyboardButton("Admin 👨🏻‍💻",callback_data = "user",url = 'https://t.me/Bekmurood'))
    button.append(res)
    return InlineKeyboardMarkup(button)



def books_name_button(cat_id):
    books = get_books_by_cat_id(cat_id)
    button = []
    res = []
    for i in books:
        res.append(InlineKeyboardButton(i[2], callback_data = i[0]))
        if len(res)==2:
            button.append(res)
            res = []
    if len(res)>0:
        button.append(res)
    button.append([InlineKeyboardButton('Orqaga 🔙',callback_data = 'back')])

    return InlineKeyboardMarkup(button)



def quant_button(soni = '0'):
    button  = []
    res = []
    button.append([InlineKeyboardButton(f"Tanlanganlar:{soni}", callback_data= "soni")])
    for i in range(1,10):
        res.append(InlineKeyboardButton(f"{i}", callback_data = f'{i}'))
        if len(res)==3:
            button.append(res)
            res = []
    button.append([InlineKeyboardButton("0",callback_data = "0")])
    res.append(InlineKeyboardButton("O'chirish ❌", callback_data = 'del'))
    res.append(InlineKeyboardButton('Tozalash 🧹', callback_data = 'clear'))
    button.append(res)
    res = []
    res.append(InlineKeyboardButton("Savatga joylash 🛒",callback_data  = 'box'))
    res.append(InlineKeyboardButton("Izlash 🔎",callback_data = 'brauzer'))
    button.append(res)
    button.append([InlineKeyboardButton("Orqaga 🔙",callback_data = 'nazad')])
    return InlineKeyboardMarkup(button)



def admin_button():
    button = [
        ['Kategoriya qo\'shish'],
        ['Mahsulot qo\'shish'],
        ['Asosiy Menuga o\'tish'],
        ['Statistika','Reklama']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,  one_time_keyboard = True)

def category_button():
    data = books_category_select()
    button  = []
    res = []
    for i in data:
        res.append(InlineKeyboardButton(i[1], callback_data = i[0]))
        if len(res)==2:
            button.append(res)
            res = []
    if len(res)>0:
        button.append(res)
    return InlineKeyboardMarkup(button)




def button_box(ord_det):
    button = []
    res = []
    
    for i in ord_det:
        product = get_books(i[2])
        res.append(InlineKeyboardButton("➕",callback_data = f"plus_{i[0]}"))
        res.append(InlineKeyboardButton(f"{product[2]}",callback_data = 'name'))
        res.append(InlineKeyboardButton("➖",callback_data= f"minus_{i[0]}"))
        button.append(res)
        res = []

    button.append([InlineKeyboardButton('Buyurtmani tasdiqlash',callback_data = "confirm")])
    button.append([InlineKeyboardButton("Yana buyurtma berish",callback_data = 'retry')])

    return InlineKeyboardMarkup(button)


def locat_button():
    button = [
        [KeyboardButton("Joylashuvni yuborish", request_location= True)]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,one_time_keyboard = True)


def check_button_locat():
    button = [
        ["Tasdiqlash",KeyboardButton("Qayta yuborish",request_location = True)]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,one_time_keyboard = True)


def history_button():
    button=[]
    button.append([InlineKeyboardButton("Clear history 🧹",callback_data = "cls")])
    button.append([InlineKeyboardButton("Orqaga 🔙",callback_data = 'back_home')])
    return InlineKeyboardMarkup(button)

