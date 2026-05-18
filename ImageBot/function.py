from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext
from database import *
from button import admin_button

#the starting part of the bot 
admins = [1306354017]
def start(update:Update,context:CallbackContext):
    if update.effective_user.id in admins:
        update.message.reply_text(f"<b>{update.effective_user.first_name} siz botning adminisiz</b>",reply_markup = admin_button(),parse_mode = "HTML")
        return 'state_admin_panel'
    else:
        update.message.reply_text("<b>Rasm yuboring,men uni o'zgartirib beraman</b>",parse_mode = 'HTML')
        if get_user_id(update.effective_user.id):
            return 'get_user_photo'
        else:
            save_users(update.effective_user.id,update.effective_user.first_name)
            return 'get_user_photo'


def channel_post(update,context):
    msg = update.channel_post
    if msg:
        print(msg)

#Admin panel part of the bot
def admin_function(update:Update,context:CallbackContext):
    data = update.message.text
    
    if data == 'Reklama 📱':
        update.message.reply_text("<b>Reklamangizni yuboring</b>",parse_mode = 'HTML')
        return "state_send_reklama"

    elif data == 'Statistika 🧮':
        users = count_users()
        update.message.reply_text(f"<b>Botdagi obunachilar soni {len(users)} ta </b>",parse_mode = 'HTML')
        return 'state_admin_panel'
    elif data == 'Asosiy qism':
        update.message.reply_text("<b>Botga rasm yuboring,men uni o'zgartirib beraman</b>",parse_mode = 'HTML')
        return 'get_user_photo'
    elif data == 'Javob ➡️':
        update.message.reply_text(f"<b>Javobni 'Reply' shaklda yuboring\nAdmin panelga qaytish uchun\nstart {'/start'} buyrug'ini bosing</b>",parse_mode = 'HTML')
        return 'state_send_photo'

#reklama part of the bot
def send_reklama(update:Update,context:CallbackContext):
    message = update.message
    users = count_users()
    error_list = ['Reklama 📱','Statistika 🧮','Javob ➡️']
    for i in users:
        if update.message.text in error_list:
            update.message.reply_text('Xato reklama,qaytadan yuboring')
            return 'state_send_reklama'
        else:
            print(message)
            if message.text:
                context.bot.sendMessage(i[1],message.text)
            elif message.photo:
                context.bot.sendPhoto(i[1],photo = message.photo[-1].file_id,caption = message.caption)
            elif message.video:
                context.bot.sendVideo(i[1],message.video.file_id,caption = message.caption)
            elif message.voice:
                context.bot.sendAudio(i[1],message.voice.file_id,caption = message.caption)
            elif message.audio:
                context.bot.sendAudio(i[1],message.audio.file_id,caption = message.caption)
            else:
                update.message.reply_text('<b>Iltimos faqat rasm,text,audio,video\nformatdagi reklamalardan foydalaning</b>',parse_mode= 'HTML')
                return "state_send_reklama"
    update.message.reply_text("Reklama yuborildi ✅",reply_markup = admin_button())
    return "state_admin_panel"


def get_user_data(update:Update,context:CallbackContext):
    msg = update.message
   
    try:
        context.bot.sendPhoto(chat_id = 1306354017,photo = msg.photo[-1].file_id,caption = f"{update.effective_user.id}")
        # context.bot.sendPhoto(chat_id = 5381432442,photo = msg.photo[-1].file_id,caption = f"{update.effective_user.id}")        
        update.message.reply_text("<b>Rasm yuborildi javobni kuting</b>",parse_mode = 'HTML')
        return 'get_user_photo'
    except:
        update.message.reply_text('<b>Xatolik ❌\nfaqat rasm yuboring</b>',parse_mode = 'HTML')
        return 'get_user_photo'



def send_message_to_user(update:Update,context:CallbackContext):
    msg = update.message
    print(msg)
    if msg.photo: 
        try:
            context.bot.sendPhoto(chat_id = msg.reply_to_message.caption,photo = msg.photo[-1].file_id)
            update.message.reply_text("<b>Javob yetkazildi</b> ✅",parse_mode = 'HTML')
            return  "state_send_photo"
        except:
            update.message.reply_text("<b>Xatolik ❌\njavobingizni 'Reply' shaklda yuboring</b>",parse_mode = 'HTML')
            return 'state_send_photo'
    else:
        update.message.reply_text("<b>Siz rasm yubormadingiz ❌\nTekshirib qaytadan yuboring</b>",parse_mode = 'HTML')
        return "state_send_photo"

