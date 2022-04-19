from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler
import logging
from telegram import Update
from telegram.error import Unauthorized
from telegram.ext.dispatcher import run_async
from random import randint
import db
from datetime import datetime
import time
import pytz
import asyncio
import aioschedule


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
    message = randDroch()
    context.bot.send_message(chat_id=update._effective_chat.id, text=message)

def randDroch():
    rand = randint(0, 100)
    if rand < 50:
        message = "NE DROCHIT` SEGONDYA"
    else:
        message = "DROCHI SEGODNYA"
    return message

def randGif():
    pass

#почему при переборе циклом происходит хуета?
# это было из-за экзепшинов телеги
#1460969666	18.04.22	19:54:27

def job(context):
    users = db.search_db()
    now_all = get_date()
    now_date, now_time = now_all.split()
    now_date = datetime.strptime(now_date, "%d.%m.%y")
    now_time = datetime.strptime(now_time, "%H:%M:%S")
    for i in users:
        try:
            updater.bot.send_message(i[0], 'PRIVET')
            date = datetime.strptime(i[1], "%d.%m.%y")
            time = datetime.strptime(i[2], "%H:%M:%S")

            diff_btw_dates = now_date - date

            if(str(diff_btw_dates) == "1 day, 0:00:00"):
                if(now_time <= time):
                    format_now_date = datetime.strftime(now_date, "%d.%m.%y")
                    format_now_time = datetime.strftime(now_time, "%H:%M:%S")
                    db.update_table_db(i[0], format_now_date, format_now_time)

                    message = randDroch()
                    gif = randGif()

                    updater.bot.send_message(i[0], message)
        except Unauthorized:
            db.delete_from_db(i[0])

def get_date():
    current_dt = datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d.%m.%y %H:%M:%S")
    return current_dt



# по прежднему не работает асинхронно я пошел спать
# Асинхронность или много поточность?
# async def scheduler():
#     aioschedule.every(3).seconds.do(job)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# def sendAsync():
#     loop = asyncio.get_event_loop()
#     loop.create_task(scheduler())
#     loop.run_forever()


# dispatcher.run_async(scheduler())




tellMe_handler = CommandHandler('tellMe', tellMe)

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(tellMe_handler)


def scheduler():
    aioschedule.every(3).seconds.do(job)
    while True:
        aioschedule.run_pending()
        asyncio.sleep(1)


updater.job_queue.run_repeating(job, 60)


updater.start_polling()
updater.idle()


