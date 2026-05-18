from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup


def admin_button():
    button = [
        ['Reklama 📱','Statistika 🧮'],
        ['Javob ➡️','Asosiy qism']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,one_time_keyboard = False)