
from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext
from database import *
from button import *






def start(update:Update,context:CallbackContext):
    #O'zgarish_1
    admins = [1306354017]

    if update.effective_user.id in admins:
        update.message.reply_text(f"<b>{update.effective_user.first_name} siz adminsiz 👇</b>", reply_markup = admin_panel_button(),parse_mode = "HTML")
        return "state_command_admin"
    else:
        update.message.reply_text(f"<b>Assalomu Alaykum {update.effective_user.first_name} botimizga xush kelibsiz. O'zingizga kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = 'HTML')
        if get_user_id(update.effective_user.id):
            return 'state_main_command'
        else:
            insert_table_user(update.effective_user.id,update.effective_user.first_name)
            return 'state_main_command'








#### Asosiy Menu
def main_command(update:Update,context:CallbackContext):
    data = update.message.text

    if data == 'Namoz vaqtlari 🕔':
        update.message.reply_text('<b>Quyidagi tugmalardan birini tanlang 🔢↙️</b>',reply_markup = namaz_time_button(),parse_mode= 'HTML')
        return 'state_namaz_time'
            
    elif data == 'Savol yuborish❓':
        update.message.reply_text('<b>Savolingizni matn ko\'rinishida yuboring</b>',parse_mode = 'HTML')
        return "state_get_answer"

    elif data=='Tasbeh 📿':
        update.message.reply_text('33 <-- سبحان الله. SubhanAllah',reply_markup = tasbeh_button1())
        context.user_data['soni'] = 0
        return 'state_tasbeh'

    elif data == 'Juma maruzasi mp3🎧':
        id = 1
        try:
            name = get_juma_maruza(id)[1]
            update.message.reply_text("Fayl yuklanguncha biroz kuting...")
            update.message.reply_audio(open(f"audio/{name}.mp3","rb"),caption = f"{name}.Juma maruzasi")
            return "state_main_command"
        except:
            update.message.reply_text("Audio fayl hali qo'shilmadi ❌")
            return "state_main_command"

    elif data =='Masjid haqida 💡':
        #O'zgarish_2
        xabar = f"""<b>
Farg'ona viloyati Buvayda tumanidagi\nPoshshopirim qishlog'i 
nafaqat shirin anjirlari, balki tarixiy obidalari, 
ziyoratgohlari bilan ham mashhur. 
Xalq tilida “Poshshopirim” ziyoratgohi deb tanilgan 
Shoh Muhammad ibn Jarir tarixiy obidasi devorlariga 
ishlangan dastlabki bezaklar VIII-IX 
asrlarga taalluqli bo'lib, birgina shu jihatning 
o'zi ham bu qishloq nechog'li qadimiy ekanligidan dalolatdir. 
Qishloqning o'ziga xos ramzi bo'lgan ziyoratgohning 
kirish qismida Temuriylar sulolasi qurdirgan 
maqbara saqlanib qolgan. Tarixiy 
maskan ichkarisida XIX asrga oid binolar bor. 
Yigirma bir metrli minora esa bir necha yuz yillar mobaynida 
e'tiqodda sobit buvaydaliklar uchun pok iymon ramzi bo'lib kelmoqda.\n
TEL:📞+998941386602 +998945512203
REKLAMA UCHUN: @sabr_uchun</b>"""
    
        update.message.reply_text(xabar,reply_markup = local_button(),parse_mode = "HTML")
        return 'state_local_back'
        

        
    elif data =='Ijtimoiy tarmoqlar 🌐':
        update.message.reply_text('<b>Ijtimoiy tarmoqlarimiz</b>',reply_markup = admin_button(), parse_mode = 'HTML')
        return 'state_admin_back'

    elif data == "Surah mp3🎧":
        update.message.reply_text("<b>Ushbu bo'lim tez orada qo'shiladi...</b>",parse_mode = "HTML")
        return "state_main_command"

    elif data== "Reyting 📈":
        update.message.reply_text("<b>Botimiz faoliyatini baholang 📝</b>",reply_markup = reyting_button(),parse_mode = "HTML")
        return "state_get_reyting"

### Asosiy menu








### Namoz Vaqtlari 
def namaz_time(update:Update,context:CallbackContext):
    data = update.message.text 
    if data == 'O\'zbekiston bo\'yicha 🇺🇿':
        try:
            photo_name1 = select_namaztime_uzb()[1]
            xabar2 = "O'zbekiston bo'yicha 🇺🇿"
            update.message.reply_photo(open(f"uzb_photos/{photo_name1}.jpg",'rb'),caption = f"<b>{xabar2}\n{photo_name1} kungi namoz vaqtlari</b>",parse_mode = "HTML")
        except:
            photo_name1 = select_namaztime_uzb()[1]
            xabar2 = "O'zbekiston bo'yicha 🇺🇿"
            update.message.reply_text(f"<b>{xabar2}\n{photo_name1} kungi namoz vaqtlari</b>",parse_mode = "HTML")
                
    elif data == 'Poshshopirim masjidi 🕌':
        try:
            photo_name2 = select_namaztime_posh()[1]
            xabar = "Poshshopirim masjidi  🕌"
            update.message.reply_photo(open(f"posh_photos/{photo_name2}.jpg",'rb'),caption = f"<b>{xabar}\n{photo_name2} kungi namoz vaqtlari</b>",parse_mode = "HTML")
        except:
            photo_name2 = select_namaztime_posh()[1]
            xabar = "Poshshopirim masjidi  🕌"
            update.message.reply_text(f"<b>{xabar}\n{photo_name2} kungi namoz vaqtlari</b>",parse_mode = "HTML")
    elif data=="Orqaga 🔙":
        update.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
        return 'state_main_command'
    






#### Orqaga qismlari         
def admin_back(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    try:
        if data== 'admin_back':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_admin_back"

def local_back(update:Update,context:CallbackContext):
    data = update.message.text
    if data == 'Orqaga 🔙':
        update.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
        return 'state_main_command'
    





#### Tasbeh Bo'limi 
def tasbeh_command(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    try:
        if data == 'tasbeh_back1':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
        elif data=='zikr1' :  
            soni = context.user_data['soni']+1
            context.user_data['soni'] = soni
            query.message.edit_reply_markup(reply_markup = tasbeh_button1(soni))
            if context.user_data['soni']==33:
                query.message.delete()
                query.message.reply_text("33 <-- الحمد لله Alhamdulillah",reply_markup = tasbeh_button2())
                return 'state_tasbeh2'
        context.user_data['soni2'] = 0
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_tasbeh"

def tasbeh_command2(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    try:
        if data == 'tasbeh_back2':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
        elif data =='zikr2':
            soni = context.user_data['soni2']+1
            context.user_data['soni2'] = soni
            query.message.edit_reply_markup(reply_markup = tasbeh_button2(soni))
            if context.user_data['soni2']==33:
                query.message.delete()
                query.message.reply_text("33 <-- الله أكبر Allohu Akbar",reply_markup = tasbeh_button3())
                return 'state_tasbeh3'
        context.user_data['soni3'] = 0
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_tasbeh2"


def tasbeh_command3(update:Update,context:CallbackContext):
    query  = update.callback_query
    data = query.data
    try:
        if data == 'tasbeh_back3':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
        elif data == 'zikr3':
            soni = context.user_data['soni3']+1
            context.user_data['soni3'] = soni
            query.message.edit_reply_markup(reply_markup = tasbeh_button3(soni))
            if context.user_data['soni3'] == 33:
                query.message.delete()
                query.message.reply_text("<b>La ilaha illallohu vahdahu la sharika lah, lahul mulku va lahul hamd. Va huva 'ala kulli shayin qodir.</b>",reply_markup = main_button(),parse_mode = 'HTML')
                return 'state_main_command'
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_tasbeh3"
####Tasbeh bo'limi




        


### Admin Panel ###

def admin_command(update:Update, context:CallbackContext):
    data = update.message.text
    #O'zgarish_3
    main_admin  = [1306354017]
    if data == '➕ Namoz vaqti 🕔':
        if update.effective_user.id in main_admin:
            update.message.reply_text("<b>Manzilni tanlang</b> 👇",reply_markup = namaz_time_button_admin(),parse_mode = "HTML")
            return 'state_admin_namaz_time'
        else:
            update.message.reply_text("Photo is already added ✅ ")
            return "state_command_admin"

    elif data=="➕ Juma maruzasi mp3🎧":
        if update.effective_user.id in main_admin:
            update.message.reply_text("<b>Maruza sanasini yuboring.\n(kun.oy.yil)</b>",parse_mode = "HTML")
            return "state_add_juma_maruza"
        else:
            update.message.reply_text("File audio already added ✅")
            return "state_command_admin"

    elif data == "Reklama📱":
        if update.effective_user.id in main_admin:
            update.message.reply_text("Reklama yuborishingiz mumkin.",reply_markup = ReplyKeyboardRemove())
            return "state_send_reklama"
        else:
            update.message.reply_text("Reklama vaqtincha to'xtatilgan ❌")
            return "state_command_admin"
    elif data == 'Javob ➡️':
        update.message.reply_text(f"<b>Javobni 'Reply' shaklda yuboring\nAdmin panelga qaytish uchun\nstart {'/start'} buyrug'ini bosing</b>",parse_mode = 'HTML')
        return 'state_send_answer'
        

    elif data == "Statistika 🧮":
        users = count_users()
        update.message.reply_text(f"<b>Botdagi obunachilar soni {len(users)} ta </b>",parse_mode = 'HTML')

    elif data == "Asosiy menu":
        update.message.reply_text(f"<b>Assalomu Alaykum {update.effective_user.first_name} botimizga xush kelibsiz. O'zingizga kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = 'HTML')
        if get_user_id(update.effective_user.id):
            return 'state_main_command'
        else:
            insert_table_user(update.effective_user.id,update.effective_user.first_name)
            return 'state_main_command'
    
    elif data == "Reyting 📈":
        baho = statistika_reyting()
        main_baho = 0
        for i in baho:
            main_baho+=int(i[2])
        update.message.reply_text(f"Umumiy reyting {main_baho}")
        return "state_command_admin"






def admin_namaz_time(update:Update,context:CallbackContext):
    data = update.message.text
    try:
        if  data == 'Poshshopirim vaqti bo\'yicha 🕌':
            update.message.reply_text("<b>Namoz vaqtlarini sanasi yuboring (kun.oy.yil)</b>",parse_mode = "HTML")
            return "state_namaz_time_name"

        elif data=='O\'zbekiston vaqti bo\'yicha 🇺🇿':
            update.message.reply_text("<b>Namoz vaqtlarini sanasi yuboring (kun.oy.yil)</b>",parse_mode = "HTML")
            return "state_namaz_time_name2"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_admin_namaz_time"
        

# Poshshopirim vati bo'yicha namoz vaqtlarini qo'shish
def admin_namaz_time_name(update:Update,context:CallbackContext):
    text = str(update.message.text)
    try:
        if len(text) == 10 and int(text[:2]) <= 31 and len((text[6:]))==4 and len(text[3:5])==2 and 0<int(text[3:5])<=12:
            context.user_data['sana'] = text
            update.message.reply_text("<b>Rasm yuborishingiz mumkin</b>",parse_mode = 'HTML')
            return "state_add_namaz_time"
        else:
            update.message.reply_text("Noto'g'ri formatdagi sana. Qaytadan yuboring\n(namuna:02.02.2022) (kun.oy.yil)")
            return "state_namaz_time_name"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_namaz_time_name"

def add_namaz_time(update:Update,context:CallbackContext):
    nums =1 
    delete_posh(nums)
    update.message.photo[-1].get_file().download(f"posh_photos/{context.user_data['sana']}.jpg")
    add_image_time_posh(context.user_data['sana'])
    update.message.reply_text('<b>Namoz vaqtlari muvaffaqiyatli qo\'shildi ✅</b>',reply_markup = admin_panel_button(),parse_mode = "HTML")
    return 'state_command_admin'

# O'zbekiston vaqti bo'yicha namoz vaqtlarini qo'shish
def admin_namaz_time_name2(update:Update,context:CallbackContext):
    dat = str(update.message.text)
    try:
        if len(dat) == 10 and int(dat[:2]) < 31 and len((dat[6:]))==4 and len(dat[3:5])==2 and 0<int(dat[3:5])<=12:
            context.user_data['sana2'] = dat
            update.message.reply_text("<b>Rasm yuborishingiz mumkin</b>",parse_mode = 'HTML')
            return "state_add_namaz_time2"
        else:
            update.message.reply_text("Noto'g'ri formatdagi sana. Qaytadan yuboring\n(namuna:02.02.2022) (kun.oy.yil)")
            return "state_namaz_time_name2"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_namaz_time_name2"

def add_namaz_time2(update:Update,context:CallbackContext):
    num=1
    delete_uzb(num)
    update.message.photo[-1].get_file().download(f"uzb_photos/{context.user_data['sana2']}.jpg")
    add_image_time_uzb(context.user_data['sana2'])
    update.message.reply_text('<b>Namoz vaqtlari muvaffaqiyatli qo\'shildi ✅</b>',reply_markup = admin_panel_button(),parse_mode = "HTML")
    return 'state_command_admin'


# Juma Maruzasini qo'shish
def add_juma_maruza(update:Update,context:CallbackContext):
    text = str(update.message.text)
    try:
        if len(text) == 10 and 0 < int(text[:2]) < 31 and len((text[6:]))==4 and len(text[3:5])==2 and 0<int(text[3:5])<=12:
            update.message.reply_text("Audio formatdagi faylni yuboring")
            context.user_data['date_juma'] = text
            return "state_add_juma_maruza_audio"
        else:
            update.message.reply_text("Noto'g'ri formatdagi sana.Qaytadan yuboring\n(namuna:02.02.2022) (kun.oy.yil)")
            return "state_add_juma_maruza"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_add_juma_maruza"

     

def add_juma_maruza_audio(update:Update,context:CallbackContext):
    delete_juma_maruza(1)
    update.message.audio.get_file().download(f"audio/{context.user_data['date_juma']}.mp3")
    add_juma_maruza_name(context.user_data['date_juma'])
    update.message.reply_text("Audio fayl muvaffaqiyatli qo'shildi ✅",reply_markup = admin_panel_button())
    return "state_command_admin"



#### Admin Panel ####








# savol javob bo'limi

def get_answer(update:Update,context:CallbackContext):
    answer  = update.message
    print(answer)
    addlist = ["Namoz vaqtlari 🕔","Savol yuborish❓",'Juma maruzasi mp3🎧','Tasbeh 📿','Masjid haqida 💡','Ijtimoiy tarmoqlar 🌐','Reyting 📈']
    if answer.text in addlist:
        update.message.reply_text("<b>Xato savol ❌.\nSavolni matn ko'rinishida yuboring</b>",parse_mode = "HTML")
        return "state_get_answer"
    else:
        context.bot.send_message(chat_id = 1306354017,text = f"{answer.text}\nID:{answer.chat.id}")
        update.message.reply_text("<b>Savolingiz yuborildi\nboshqa savolingiz bo'lmasa OK tugmasini bosing 👇</b>",reply_markup = ans_button() ,parse_mode = 'HTML')
        return "state_ok_get_ans"
    

def send_answer_the_ques(update:Update,context:CallbackContext):
    msg = update.message
    try:
        if msg:
            context.bot.send_masssage(chat_id = msg.reply_to_message.chat.id,text = msg.text)
            return "state_send_answer"
    except:
        update.message.reply_text("Avval savolni reply qiling")
        return "state_get_answer"
    
def ok_button(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    query.message.delete()
    if data == "ok":
        context.bot.answerCallbackQuery(query.id,"Botimizdan foydalanganingiz uchun rahmat 🤗",show_alert = True)
        return "state_main_command"
    elif data == 'retry':
        query.message.reply_text('<b>Savolingizni matn ko\'rinishida yuboring</b>',parse_mode = 'HTML')
        return "state_get_answer"


####Reklama qismi

def send_reklama(update:Update,context:CallbackContext):
    message = update.message
    users = count_users()
    for i in users:
        try:
            context.bot.forward_message(i[1],update.effective_user.id,message.message_id)
        except Exception as e:
            print(e)
    update.message.reply_text("Reklama yuborildi ✅",reply_markup = admin_panel_button())
    return "state_command_admin"

    
    

#Baholash qismi
def get_reyting(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    if data.isdigit():
        if check_reyting(update.effective_user.id):
            query.message.delete()
            context.bot.answerCallbackQuery(query.id,"Siz avval botimizni baholagansiz 😊",show_alert = True,)
            return "state_main_command"
        else:
            query.message.delete()
            add_reyting_road(update.effective_user.id,int(data))
            context.bot.answerCallbackQuery(query.id,"Baho uchun rahmat 🙂,biz bilan qoling!",show_alert = True)
            return "state_main_command"
    elif data == "restart":
        if check_reyting(update.effective_user.id):
            query.message.delete()
            delete_reyting(update.effective_user.id)
            context.bot.answerCallbackQuery(query.id,"Qayta baholashingiz mumkin 😊",show_alert = True)
            query.message.reply_text("<b>Qayta baholashingiz mumkin 🔁</b>",reply_markup = reyting_button(),parse_mode = "HTML")
            return "state_get_reyting"
        else:
            context.bot.answerCallbackQuery(query.id,"Sizda baho mavjud emas.Botimizni baholang 👇",show_alert = True )
            return "state_get_reyting"
    elif data == "reyting_back":
        query.message.delete()
        query.message.reply_text(f"<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = 'HTML')
        return "state_main_command"


