from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton

def main_button():
    button = [
        ["E'lon joylash 📝"],
        ['Statistika 📊'],
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)
    
# def delete_button():
#     button = [
#         [InlineKeyboardButton("Qayta yuklash",callback_data = 'redeploy')],
#         [InlineKeyboardButton("Delete",callback_data = 'del_data')]

#     ]
#     return InlineKeyboardMarkup(button)

def viloyatlar():
    button = [
        ['Toshkent shahri'],
        ['Andijon',"Namangan"],
        ["Farg'ona",'Toshkent'],
        ['Sirdaryo','Jizzah'],
        ['Samarqand','Buxoro'],
        ['Qashqadaryo','Surxondaryo'],
        ['Navoiy','Xorazm'],
        ['Orqaga 🔙']
       
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def staff_sex():
    button = [
        ["Erkak",'Ayol'],
        ["Bekor qilish ❌"]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)
def phone_button():
    button = [      
        [KeyboardButton('Share to contact',request_contact = True)]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def chek_button():
    button = [
        ["To'g'ri","Noto'g'ri"]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def cancel_button():
    button = [
        ["Bekor qilish ❌"]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def get_degree_button():
    button = [
        ['Oliy',"O'rta maxsus"],
        ["Bekor qilish ❌"]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)


def admin_button():
    button = [
        ['Reklama',"Asosiy sahifa"],
        ['Del']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def viloyatlar_view():
    button = [
        ['Toshkent shahri'],
        ['Andijon',"Namangan"],
        ["Farg'ona",'Toshkent'],
        ['Sirdaryo','Jizzah'],
        ['Samarqand','Buxoro'],
        ['Qashqadaryo','Surxondaryo'],
        ['Navoiy','Xorazm']
       
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def admin_button_2():
    button = [
        ["Reklama","Asosiy bo'lim"]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)