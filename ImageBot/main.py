from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
from function import *  # Assuming your custom functions are here

# handler
conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start)
    ],
    states={
        'state_admin_panel': [
            CommandHandler('start', start),
            MessageHandler(filters.TEXT, admin_function),
        ],
        'state_send_reklama': [
            CommandHandler('start', start),
            MessageHandler(filters.ALL, send_reklama),
        ],
        'get_user_photo': [
            CommandHandler('start', start),
            MessageHandler(filters.ALL, get_user_data),
        ],
        'state_send_photo': [
            CommandHandler('start', start),
            MessageHandler(filters.ALL, send_message_to_user),
        ]
    },

    fallbacks=[
        CommandHandler('start', start)
    ]
)

get_post = MessageHandler(filters.ALL, channel_post)

# Bot token
token = '5998755347:AAEWBBayo1Raa_C4TzJp0E1B3c5m4bR247k'

# Create the Application with your bot's token
application = Application.builder().token(token).build()

# Add handlers to the dispatcher
application.add_handler(conv_handler)
application.add_handler(get_post)

# Start polling and run
