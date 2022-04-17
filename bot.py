from telegram.ext import Updater, CallbackContext
import logging
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from random import randint
import schedule
import db
from datetime import datetime
import time
import pytz


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(
    token="5172964561:AAH872tfvkZ-D7ac5EEgDCim3kvxGOqW9SE", use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    text = 'False'
    c_date, c_time = get_date().split()
    print(type(update.effective_chat.id))
    db.add_to_db(update.effective_chat.id, str(c_date), str(c_time))


def tellMe(update: Update, context: CallbackContext):
    rand = randint(0, 100)
    if rand < 50:
        message = "NE DROCHIT` SEGONDYA"
    else:
        message = "DROCHI SEGODNYA"
    context.bot.send_message(chat_id=update._effective_chat.id, text=message)


def job():
    users = db.search_db()
    now_date, now_time = get_date().split()
    now_date = datetime.strptime(now_date, "%d.%m.%y")
    now_time = datetime.strptime(now_time, "%H:%M:%S")
    for i in users:

        date = datetime.strptime(i[1], "%d.%m.%y")
        time = datetime.strptime(i[2], "%H:%M:%S")

        diff_btw_dates = now_date - date

        if(str(diff_btw_dates) == "1 day, 0:00:00"):
            if(now_time <= time):
                format_now_date = datetime.strftime(now_date, "%d.%m.%y")
                format_now_time = datetime.strftime(now_time, "%H:%M:%S")
                db.update_table_db(i[0], format_now_date, format_now_time)
                updater.bot.send_message(i[0], 'PRIVET BLYAT')


def get_date():
    current_dt = datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d.%m.%y %H:%M:%S")
    return current_dt


tellMe_handler = CommandHandler('tellMe', tellMe)

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(tellMe_handler)

# schedule.every().hour.do(job)

# асинхронный schedule ;)

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
updater.start_polling(allowed_updates=Update.ALL_TYPES)
updater.idle()
