from telegram import Update,ReplyKeyboardRemove,Bot,InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from telegram.ext import CallbackContext,CallbackQueryHandler
from button import *
from database import *
from telegram.ext import Updater
import logging


TOKEN = "6415755923:AAEWFqJF-wcPSuyuuaN_gUoUdKbqzhU9Fxk"
bot = Bot(token="7109903675:AAFss3QjI9VPFe1e5QkOXzygo_nSeAIgroc")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
admin = [1218689073,1306354017]


def start_bot1(update:Update,context:CallbackContext):
    if update.message.from_user.id in admin:
        data = getting_for_using(update.effective_user.id)
        if data:
            update.message.reply_text(f"{update.effective_user.first_name} siz bot adminisiz",reply_markup = admin_button())
            user  = update.effective_user
            if user.username:
                username = f"@{user.username}"
                context.user_data['username'] = username
                return "admin_section"
            else:
                context.user_data['username'] = user.first_name
                return "admin_section"
        else:
            update.message.reply_text(f"{update.effective_user.first_name} siz bot adminisiz",reply_markup = admin_button())
            insert_table_for_using(update.effective_user.id,update.effective_user.first_name)
            user  = update.effective_user
            if user.username:
                username = f"@{user.username}"
                context.user_data['username'] = username
                return "admin_section"
            else:
                context.user_data['username'] = user.first_name
                return "admin_section"
    else:
        data = getting_for_using(update.effective_user.id)
        if data:
            update.message.reply_text("Kerakli bo'limni tanlang 👇",reply_markup = main_button())
            user  = update.effective_user
            if user.username:
                username = f"@{user.username}"
                context.user_data['username'] = username
                return "main_command"
            else:
                context.user_data['username'] = user.first_name
                return "main_command"
        else:
            update.message.reply_text("K erakli bo'limni tanlang 👇",reply_markup = main_button())
            insert_table_for_using(update.effective_user.id,update.effective_user.first_name)
            user  = update.effective_user
            if user.username:
                username = f"@{user.username}"
                context.user_data['username'] = username
                return "main_command"
            else:
                context.user_data['username'] = user.first_name
                return "main_command"
############Admin
def admin_func(update:Update,context:CallbackContext):
    data = update.message.text
    context.user_data['username'] = update.effective_user.first_name
    if data == "Reklama":
        update.message.reply_text("Menga o'z reklamangizni yuboring\nMen uni barchaga yuboraman")
        return "state_get_rec"
    elif data == "Asosiy sahifa":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button())
        return "main_command"      
    elif data ==  "Del":
        send_message_with_delete_button(context)

def get_rec(update:Update,context:CallbackContext):
    message = update.message
    users = getting_users()
    error_list_2 = ["Asosiy sahifa","Reklama"]
    if users:
        if update.message.text in error_list_2:
            update.message.reply_text('Xato reklama,qaytadan yuboring')
            return 'state_get_rec'
        else:
            for i in users:
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
                    return "state_get_rec"
        update.message.reply_text("Reklama yuborildi ✅")
        return "admin_section"       
    else:
        update.message.reply_text("Botda hali obunachi mavjud emas")
        return "admin_section"
#################
def main_com(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "E'lon joylash 📝":
        context.user_data['id'] = update.effective_user.id
        update.message.reply_text("Xududingizni tanlang",reply_markup = viloyatlar())
        return "state_area"

    elif data == "Statistika 📊":
        users = getting_users()
        update.message.reply_html(f"Botdagi foydalanuvchilar soni <b>{len(users)}ta</b>")
        return "main_command"
    


def get_area(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Orqaga 🔙":
        update.message.reply_text("Marhamat,kerakli bo'limni tanlang", reply_markup = main_button())
        return "main_command"
    elif data in ['Toshkent shahri','Andijon',"Namangan","Farg'ona",'Toshkent','Sirdaryo','Jizzah','Samarqand','Buxoro','Qashqadaryo','Surxondaryo','Navoiy','Xorazm']:
        context.user_data['viloyat'] = data
        update.message.reply_text("Telefon raqamingizni yuboring",reply_markup = phone_button())
        return "state_get_phone"
    else:
        return "state_area"
    
    
def get_phone(update:Update,context:CallbackContext):
    data = update.message
    
    if data.contact.phone_number:
        update.message.reply_text("Xodim turini kiriting",reply_markup = staff_sex())

        context.user_data['phone_number'] = data.contact.phone_number
        return "get_staff_sex"
    else:
        return "state_get_phone"

def get_staff_state(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    elif data in ["Erkak",'Ayol']:
        context.user_data['staff_sex'] = data
        update.message.reply_text("Xodim malumotini kiriting\n(Oliy yoki o'rta maxsus)",reply_markup = get_degree_button())
        return "state_get_degree"
    else:
        return "get_staff_sex"

def get_degree(update:Update,context:CallbackContext):
    data = update.message.text
    if data  == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    elif data in  ['Oliy',"O'rta maxsus"]:
        update.message.reply_text("Kerakli xodimni tanlang\n(Masalan:Xamshira yoki Dasturchi)",reply_markup = cancel_button())
        context.user_data['daraja'] = data
        return "state_get_jobtype"
    else:
        return "state_get_degree"

def get_jobtype(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        context.user_data['jobtype'] = data
        update.message.reply_text(f"Oylik maoshni kiriting\n(Masalan:2 mln)",reply_markup = cancel_button())
        return "state_get_salary"
def get_salary(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        context.user_data['salary'] = data
        update.message.reply_text(f"Kerakli yoshni kiriting\n(Masalan:20-30 yosh)",reply_markup = cancel_button())
        return "state_get_age"
def get_age(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        context.user_data['user_age'] = data
        update.message.reply_text(f"Kunlik ish vaqtni kiriting\n(Masalan: 08:00 dan 17:00 gacha)",reply_markup = cancel_button())
        return "state_get_dailyhour"
def get_hours(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        context.user_data['hours'] = data
        update.message.reply_text(f"Ish joyi manzilini kiriting\n(Masalan:Yunusobod tumani)",reply_markup = cancel_button())
        return "state_get_manzil"


def get_manzil(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        context.user_data['manzil'] = data
        update.message.reply_text("Xodimning vazifalarini kiriting",reply_markup = cancel_button())
        return "state_xabarchi"

def send_make_message(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        update.message.reply_text("Qo'shimcha ma'lumot kiriting",reply_markup = cancel_button())
        context.user_data['vazifalar'] = data
        return "state_get_adding"
def get_adding(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Bekor qilish ❌":
        update.message.reply_text("Quyidagi tugmalardan birini tanlang",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    else:
        message = f"""<b>🏢 Ish hududi:{context.user_data['viloyat']}\n 
🤵👩‍🦰 Xodim:{context.user_data['staff_sex']}\n 
🕡 Yosh chegarasi:{context.user_data['user_age']}\n 
🗂 Kerakli xodim:{context.user_data['jobtype']}\n 
🎓 Malumoti:{context.user_data['daraja']} \n
📃 Xodimning vazifalari:{context.user_data['vazifalar']}\n
🕰 Ish vaqti:{context.user_data['hours']}\n
🪙 Oylik maosh:{context.user_data['salary']}\n
📍 Manzil:{context.user_data['manzil']}\n
⌚️ Qo'shimcha malumot:{data}\n
📞 Telefon raqami:{context.user_data['phone_number']}\n </b>
👤 Ish beruvchi ismi:{context.user_data['username']}\n
"""
        insert_table(context.user_data['viloyat'],update.effective_user.id,context.user_data['user_age'],context.user_data['staff_sex'],context.user_data['daraja'],context.user_data['jobtype'],context.user_data['vazifalar'],context.user_data['hours'],context.user_data['salary'],context.user_data['manzil'],data,context.user_data['phone_number'],context.user_data['username'],0)
        update.message.reply_text(f"<b>{message}</b>",parse_mode = "HTML")
        context.user_data['all_message'] = message
        update.message.reply_text(f"Xabar to'g'ri ekanligini tekshiring",reply_markup = chek_button())
        return "state_check_message"
def checking(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "To'g'ri":
        context.bot.send_message("-1001929269397",context.user_data['all_message'],parse_mode = "HTML")
        # updater = Updater(token="7109903675:AAFss3QjI9VPFe1e5QkOXzygo_nSeAIgroc", use_context=True)
        area_staff = get_send_staff(context.user_data['viloyat'])
        if area_staff:
            for i in area_staff:
                bot.send_message(chat_id=i[3],text=context.user_data['all_message'],parse_mode = "HTML")
        else:
            pass
        update.message.reply_text("<b>Arizangiz muvaffaqiyatli yuborildi\n\nYana ariza berishingiz mumkin</b>",reply_markup = main_button(),parse_mode = "HTML")
        return "main_command"
    elif data == "Noto'g'ri":
        update.message.reply_text("<b>Jarayon qaytadan tuzildi 🔁\n\nXududingizni tanlang</b>",parse_mode = "HTML",reply_markup = viloyatlar())
        return "state_area"
    else:
        return "state_check_message"
    
# #########################################################################3


def start_bot2(update:Update,context:CallbackContext):
    admin_list_2 = [1218689073,1306354017]
    
    if update.effective_user.id in admin_list_2:
        checking_user = check_user_in_tableforstaff(update.effective_user.id)
        if checking_user:
            update.message.reply_text("Siz bot adminisiz",reply_markup = admin_button_2())
            return "admin_section_2"
        else:
            insert_table_for_staff(update.effective_user.id)
            update.message.reply_text("Siz bot adminisiz",reply_markup = admin_button_2())
            return "admin_section_2"
    else:
        checking_user = check_user_in_tableforstaff(update.effective_user.id)
        if checking_user:
            update.message.reply_text("Xududingizni tanlang",reply_markup = viloyatlar_view(),parse_mode = "HTML")
            return "show_jobs"
        else:
            update.message.reply_text("Xududingizni tanlang",reply_markup = viloyatlar_view(),parse_mode = "HTML")
            insert_table_for_staff(update.effective_user.id)
            return "show_jobs"

def admin_2(update:Update,context:CallbackContext):
    data = update.message.text
    if data == "Reklama":
        update.message.reply_text("Menga o'z reklamangizni yuboring\n\nMen uni hammaga yuboraman")
        return "send_rec_to_users_bot2"
    elif data == "Asosiy bo'lim":
        update.message.reply_text("Xududingizni tanlang",reply_markup = viloyatlar_view(),parse_mode = "HTML")
        return "show_jobs"

def send_rec(update:Update,context:CallbackContext):
    message = update.message
    users = get_table_for_staff()
    print(users)
    error_list = ["Asosiy bo'lim","Reklama"]
    if users:
        if update.message.text in error_list:
            update.message.reply_text('Xato reklama!\nQaytadan yuboring')
            return 'send_rec_to_users_bot2'
        else:
            for i in users:
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
                    return "send_rec_to_users_bot2"
        update.message.reply_text("Reklama yuborildi ✅")
        return "admin_section_2"       
    else:
        update.message.reply_text("Botda hali obunachi mavjud emas")
        return "send_rec_to_users_bot2"


def show_jobs(update:Update,context:CallbackContext):
    data = update.message.text
    checking = get_staff(update.effective_user.id)
    if checking:
        update_area(update.effective_user.id,data)
        if data in ['Toshkent shahri','Andijon',"Namangan","Farg'ona",'Toshkent','Sirdaryo','Jizzah','Samarqand','Buxoro','Qashqadaryo','Surxondaryo','Navoiy','Xorazm']:
            message = get_area_from_db(data)
            if message:
                adding_view(data)
                for i in message:
                    update.message.reply_text(f"""<b>🏢 Ish hududi:{i[1]}\n
🤵👩‍🦰 Xodim:{i[4]}\n
🕡 Yosh chegarasi:{i[3]}\n 
🗂 Ish turi:{i[6]}\n
🧾 Malumoti:{i[5]}\n
📜 Xodimning vazifalari:{i[7]}\n
🕰 Kunlik ish vaqti:{i[8]}\n
🪙 Oylik maosh:{i[9]}\n
n📍 Manzil:{i[10]}\n
📃 Qo'shimcha malumot:\n{i[11]}\n
📞 Telefon raqami:{i[12]}\n
👤 Ish beruvchi ismi:{i[13]}\n
👁‍🗨 Ushbu post ko'rilgan:{i[14]} marta\n</b>""",parse_mode = "HTML")
                return "show_jobs"
            else:
                update.message.reply_text(f"<b>Ushbu {data} xududi bo'yicha xali e'lonlar mavjud emas ⛔️\n\nYangi e'lon qo'shilishi bilan sizga uni e'lon qilamiz</b>",parse_mode = "HTML")
                return "show_jobs"
        else:
            return "show_jobs"

    else:
        insert_staff(update.effective_user.first_name,data,update.effective_user.id)
        if data in ['Toshkent shahri','Andijon',"Namangan","Farg'ona",'Toshkent','Sirdaryo','Jizzah','Samarqand','Buxoro','Qashqadaryo','Surxondaryo','Navoiy','Xorazm']:
            message = get_area_from_db(data)
            if message:
                adding_view(data)
                for i in message:
                    update.message.reply_text(f"""<b>🏢 Ish hududi:{i[1]}\n
🤵👩‍🦰 Xodim:{i[4]}\n
🕡 Yosh chegarasi:{i[3]}\n 
🗂 Ish turi:{i[6]}\n
🧾 Malumoti:{i[5]}\n
📜 Xodimning vazifalari:{i[7]}\n
🕰 Kunlik ish vaqti:{i[8]}\n
🪙 Oylik maosh:{i[9]}\n
📍 Manzil:{i[10]}\n
📃 Qo'shimcha malumot:\n{i[11]}\n
📞 Telefon raqami:{i[12]}\n
👤 Ish beruvchi ismi:{i[13]}\n
👁‍🗨 Ushbu post ko'rilgan:{i[14]} marta\n</b>""",parse_mode = "HTML")
                return "show_jobs"
            else:
                update.message.reply_text(f"<b>{data} xududi bo'yicha e'lonlar mavjud emas ⛔️\n\nYangi e'lon qo'shilishi bilan\nbiz sizga uni yuboramiz</b>",parse_mode = "HTML")
                return "show_jobs"
        else:
            return "show_jobs"


