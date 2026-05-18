from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

def admin_panel_button():
    button = [
        ['➕ Namoz vaqti 🕔',"➕ Juma maruzasi mp3🎧"],
        ['Reklama📱','Statistika 🧮'],
        ['Asosiy menu','Javob ➡️'],
        ['Reyting 📈'] 
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,one_time_keyboard = True)


def namaz_time_button_admin():
    button = [
        ['Poshshopirim vaqti bo\'yicha 🕌'],
        ['O\'zbekiston vaqti bo\'yicha 🇺🇿']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def main_button():
    button = [
        ['Namoz vaqtlari 🕔','Savol yuborish❓'],
        ["Juma maruzasi mp3🎧",'Tasbeh 📿'],
        ["Surah mp3🎧",'Masjid haqida 💡'],
        ['Reyting 📈','Ijtimoiy tarmoqlar 🌐']
       
        
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)


def namaz_time_button():
    button= [
        ['O\'zbekiston bo\'yicha 🇺🇿'],
        ['Poshshopirim masjidi 🕌'],
        ['Orqaga 🔙']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard =True,one_time_keyboard = False)


def admin_button():
    button = [
        [InlineKeyboardButton("Gavhar Tv 📺",url = "https://youtube.com/channel/UCG3PTy4VamJvxu5cwVK2Qlg"),InlineKeyboardButton("Poshshopirim.uz 📲",url = 'https://t.me/poshshopirmuz')],
        [InlineKeyboardButton("Islom Sohili 📲", url = "https://t.me/islom_sohili"),InlineKeyboardButton("BookStore",url = "https://t.me/Delivery_bookbot")],
        [InlineKeyboardButton('Admin 👨🏻‍💻 1', url = 'https://t.me/sabr_uchun'),InlineKeyboardButton('Admin 👨🏻‍💻 2', url = 'https://t.me/Premium_N11')],
        [InlineKeyboardButton('Orqaga 🔙', callback_data = 'admin_back')]
    ]
    return InlineKeyboardMarkup(button)

def local_button():
    button = [
        ['Orqaga 🔙']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)


def tasbeh_button1(soni = '0'):
    button = [  
        [InlineKeyboardButton(f'SubhanAllah --> [{soni}]', callback_data = 'zikr1')],
        [InlineKeyboardButton('Orqaga 🔙', callback_data = 'tasbeh_back1')]
    ]
    return InlineKeyboardMarkup(button)

def tasbeh_button2(soni = '0'):
    button = [  
        [InlineKeyboardButton(f'Alhamdulillah --> [{soni}]', callback_data = 'zikr2')],
        [InlineKeyboardButton('Orqaga 🔙', callback_data = 'tasbeh_back2')]
    ]
    return InlineKeyboardMarkup(button)

def tasbeh_button3(soni = '0'):
    button = [  
        [InlineKeyboardButton(f'Allohu Akbar --> [{soni}]', callback_data = 'zikr3')],
        [InlineKeyboardButton('Orqaga 🔙', callback_data = 'tasbeh_back3')]
    ]
    return InlineKeyboardMarkup(button)

def ans_button():
    button = [
        [InlineKeyboardButton("🆗",callback_data = "ok")],
        [InlineKeyboardButton("Yana savol yuborish 🔄",callback_data = "retry")]
    ]
    return InlineKeyboardMarkup(button)


def reyting_button():
    button  = [
        [InlineKeyboardButton("1",callback_data = "1"),InlineKeyboardButton("2",callback_data = "2"),InlineKeyboardButton("3",callback_data = '3'),InlineKeyboardButton("4",callback_data = '4'),InlineKeyboardButton("5",callback_data = '5')],
        [InlineKeyboardButton("Qayta baholash 🔁",callback_data = "restart")],
        [InlineKeyboardButton("Orqaga 🔙",callback_data ="reyting_back")]
]

    return InlineKeyboardMarkup(button)