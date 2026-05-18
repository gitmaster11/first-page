
from telegram import Update, BotCommand, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler)
import sqlite3


# Token va Admin ID
TOKEN = "8096319260:AAGk4yWb0TFCdJGScqgtZKXuQShsAOX4OW0"
ADMIN_ID = [1306354017,1292436942,6416640069]

# Database connection
def init_db():
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER UNIQUE
    )
    """)
    conn.commit()
    conn.close()

def add_group(group_id):
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO groups (group_id) VALUES (?)", (group_id,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Group already exists
    conn.close()

def get_groups():
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT group_id FROM groups")
    groups = [row[0] for row in cursor.fetchall()]
    conn.close()
    return groups

def delete_group(group_id):
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM groups WHERE group_id = ?", (group_id,))
    conn.commit()
    conn.close()

POST, DELETE_GROUP, WAIT_POST= range(3)

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in ADMIN_ID:
        buttons = [["Post Joylash"], ["Guruhlar"]]
        update.message.reply_text("Assalomu alaykum! Siz adminsiz. Tanlang:", 
                                  reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        return POST
    else:
        update.message.reply_text("Siz admin emassiz!")
        return ConversationHandler.END

def handle_post(update: Update, context: CallbackContext):
    update.message.reply_text("Post yuboring, men uni barcha guruhlarga jo'nataman:")
    return WAIT_POST

def send_post(update: Update, context: CallbackContext):
    print(update.message.chat_id)
    message = update.message
    groups = get_groups()
    print(message.chat.id)
    for group_id in groups:
        try:
            context.bot.copy_message(chat_id=group_id, from_chat_id=message.chat.id, message_id=message.message_id)
        except Exception as e:
            print(f"Xato: {e}")
    
    update.message.reply_text("✅ Post barcha guruhlarga yuborildi!")
    return start(update, context)

def list_groups(update: Update, context: CallbackContext):
    groups = get_groups()
    
    if not groups:
        update.message.reply_text("🚫 Hozircha hech qanday guruh mavjud emas.")
        return POST
    
    keyboard = [[InlineKeyboardButton(f"{group_id}", callback_data=f"delete_{group_id}")] for group_id in groups]
    keyboard.append([InlineKeyboardButton("⬅️ Orqaga", callback_data="back")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("📋 Mavjud guruhlar:", reply_markup=reply_markup)
    return DELETE_GROUP

def handle_delete_group(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == "back":
        query.message.delete()
        buttons = [["Post Joylash"], ["Guruhlar"]]
        query.message.reply_text("🏠 Asosiy menyuga qaytdik:", 
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        return POST
    
    group_id = int(query.data.split("_")[1])
    delete_group(group_id)
    query.edit_message_text(f"❌ Guruh {group_id} o'chirildi!")
    return POST

def get_group_id(update: Update, context: CallbackContext):
    chat = update.message.chat
    if chat.type in ["group", "supergroup"]:
        group_id = chat.id
        add_group(group_id)
        update.message.reply_text(f"Guruh ID: {group_id}\n✅ Guruh muvaffaqiyatli saqlandi!")
    else:
        update.message.reply_text("🚫 Bu komanda faqat guruhlarda ishlaydi.")

def unknown_message(update: Update, context: CallbackContext):
    update.message.reply_text("🚫 Noto‘g‘ri buyruq! Iltimos, pastdagi menyudan foydalaning.")

def main():
    init_db()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            POST: [
                MessageHandler(Filters.regex("^Post Joylash$"), handle_post),
                MessageHandler(Filters.regex("^Guruhlar$"), list_groups),
            ],
            WAIT_POST: [
                MessageHandler(Filters.all & ~Filters.command, send_post),
                MessageHandler(Filters.command, unknown_message),
            ],
            DELETE_GROUP: [CallbackQueryHandler(handle_delete_group)],
        },
        fallbacks=[CommandHandler("start", start)]
    )
    
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("getid", get_group_id))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()




 