from telegram.ext import Updater, CommandHandler,ConversationHandler,Filters,MessageHandler
from function import *

def main():
    # Bot token for Bot 1
    bot_token_bot1 = "6415755923:AAEWFqJF-wcPSuyuuaN_gUoUdKbqzhU9Fxk"
    updater_bot1 = Updater(bot_token_bot1, use_context=True)
    dp_bot1 = updater_bot1.dispatcher
    conv_handler = ConversationHandler(
    entry_points = [
        CommandHandler('start',start_bot1)
    ],
    states = {
        "admin_section":[
            CommandHandler("start",admin_func),
            MessageHandler(Filters.text,admin_func)
        ],
        "state_get_rec":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.all,get_rec)
        ], 
        "main_command":[
           CommandHandler('start',start_bot1),
           MessageHandler(Filters.text,main_com),
        ],
        "state_area":[
            CommandHandler('start',start_bot1),
            MessageHandler(Filters.text,get_area)
        ],
        "state_get_phone":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.contact,get_phone)
        ],
        "get_staff_sex" :[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_staff_state)
        ],
        "state_get_degree":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_degree)
        ],
        "state_get_jobtype":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_jobtype)
        ],
        'state_get_salary':[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_salary)
        ],
        "state_get_age":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_age)
        ],
        "state_get_dailyhour":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_hours)
        ],
        "state_get_manzil":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_manzil)
        ],
        "state_xabarchi":[
            CommandHandler('start',start_bot1),
            MessageHandler(Filters.all,send_make_message)
        ],
        "state_get_adding":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.text,get_adding)
        ],
        "state_check_message":[
            CommandHandler("start",start_bot1),
            MessageHandler(Filters.all,checking)
        ],
        
    },
    fallbacks = [
        CommandHandler('start',start_bot1)
    ]
)
    dp_bot1.add_handler(conv_handler)
   

    # Bot token for Bot 2
    bot_token_bot2 = "7109903675:AAFss3QjI9VPFe1e5QkOXzygo_nSeAIgroc"
    updater_bot2 = Updater(bot_token_bot2, use_context=True)
    dp_bot2 = updater_bot2.dispatcher
    conv_handler2 = ConversationHandler(
    entry_points = [
        CommandHandler('start',start_bot2)
    ],
    states = {
        "state_main":[
            CommandHandler("start",start_bot2),
            MessageHandler(Filters.text,start_bot2)
        ],
        "show_jobs":[
            CommandHandler("start",start_bot2),
            MessageHandler(Filters.text,show_jobs)
        ],
        "admin_section_2":[
            CommandHandler("start",start_bot2),
            MessageHandler(Filters.text,admin_2)
        ],
        "send_rec_to_users_bot2":[
            CommandHandler("start",start_bot2),
            MessageHandler(Filters.all,send_rec)
        ]
    },
    fallbacks = [
        CommandHandler('start',start_bot2)
    ]
)
    dp_bot2.add_handler(conv_handler2)
    updater_bot1.start_polling()
    updater_bot2.start_polling()

    updater_bot1.idle()
    updater_bot2.idle()


if __name__ == '__main__':
    main()
