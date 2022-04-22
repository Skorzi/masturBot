from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler
import logging
from telegram import Update
from telegram.error import Unauthorized
from telegram.ext.dispatcher import run_async
from random import randint, choice
import db
from datetime import datetime
import time
import pytz
import asyncio
import aioschedule
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(
    token="5172964561:AAH872tfvkZ-D7ac5EEgDCim3kvxGOqW9SE", use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    try:
        c_date, c_time = get_date().split()
        db.add_to_db(update.effective_chat.id, str(c_date), str(c_time))
        message, img = randDroch()
        context.bot.send_animation(update._effective_chat.id, img, caption=message + "\n\nКаждые 24 часа вам будет приходить напоминалка о том дрочить ли сегодня?")
    except:
        context.bot.send_message(update._effective_chat.id, "Вам уже приходит напоминалка")



def fapNow(update: Update, context: CallbackContext):
    message, img = randDroch()
    context.bot.send_animation(update._effective_chat.id, img, caption=message)

def randDroch():
    rand = randint(0, 100)
    if rand < 50:
        message = "СЕГОДНЯ БЕЗ ДРОЧКИ!"
        img = randGifNotCum()
    else:
        message = "ВРЕМЯ ПОДРОЧИТЬ"
        img = randGifLetCum()
    return message, img

def randGifNotCum():
    gifList = [
        "https://media.giphy.com/media/6yBdSRy2ZGRlsYULKl/giphy.gif",
        "https://media.giphy.com/media/nzZemq7lGJeSKUPUb9/giphy.gif",
        "https://media.giphy.com/media/C2rTKqcznowZMegiYo/giphy.gif",
        "https://media.giphy.com/media/DkXrtqovA06Sc99Kx0/giphy.gif",
        "https://media.giphy.com/media/tbFplpHgxc5sQWQcOR/giphy.gif",
        "https://media.giphy.com/media/l11Wxd4oSTvlj8QXkl/giphy.gif",
        "https://media.giphy.com/media/ifPcnMedf5Q646OCwK/giphy.gif",
        "https://media.giphy.com/media/1v0jg6Kb3bjrNGTUjR/giphy.gif",
        "https://media.giphy.com/media/M4FA173TvqcQmUjVNd/giphy.gif",
        "https://media.giphy.com/media/KCGVl15EP8o6rBYEK5/giphy.gif",
        "https://media.giphy.com/media/p5eKWnfyNkWkwtupHN/giphy.gif",
        "https://media.giphy.com/media/9YChllnaoavCMeXctB/giphy.gif",
        "https://media.giphy.com/media/Jik5S8XsNkSreLqrKQ/giphy.gif",
        "https://media.giphy.com/media/bTCgtItQLVEadXyPmK/giphy.gif",
        "https://media.giphy.com/media/n1e5mGXoxrq9LDqziw/giphy.gif",
        "https://media.giphy.com/media/HjmrZRrgtLEPW1nPM4/giphy.gif",
        "https://media.giphy.com/media/Qkr0155oVVzIyV0AbL/giphy.gif",
        "https://media.giphy.com/media/Lt4UgDcISavQ5YuW9A/giphy.gif",
        "https://media.giphy.com/media/SUdofmVviaeh9ZHt9G/giphy.gif",
    ]
    img = choice(gifList)
    return img

def randGifLetCum():
    gifList = [
        "https://media.giphy.com/media/RQkdFOrkM3mzLyDgHI/giphy.gif",
        "https://media.giphy.com/media/r09bGyAq5hty6g9fIy/giphy.gif",
        "https://media.giphy.com/media/MsAmFeyoWyomGRj0eR/giphy.gif",
        "https://media.giphy.com/media/6A2hi95lgUNx60LWgH/giphy.gif",
        "https://media.giphy.com/media/aDQbi5tQgq1Hvi3vsf/giphy.gif",
        "https://media.giphy.com/media/3AI03XmuXAfFsdpJNc/giphy.gif",
        "https://media.giphy.com/media/iK55OqQopZgEavJQgW/giphy.gif",
        "https://media.giphy.com/media/aczNIbkcn4xVBYLjpa/giphy.gif",
        "https://media.giphy.com/media/KSIi4Engldq7u6vtYa/giphy.gif",
        "https://media.giphy.com/media/4kbF8pbEqaDgh6HiwP/giphy.gif",
        "https://media.giphy.com/media/olpqjyOow12fOf511H/giphy.gif",
        "https://media.giphy.com/media/JtgOpm347DnnyLY8rj/giphy.gif",
        "https://media.giphy.com/media/mUhaY5dF7eIb16dodg/giphy.gif",
        "https://media.giphy.com/media/3H1oQG40MRe2yOcODk/giphy.gif",
        "https://media.giphy.com/media/Ol3VsLzgjQlc6NiMtP/giphy.gif",
        "https://media.giphy.com/media/ep7973qv3xDAxTBhcM/giphy.gif",
        "https://media.giphy.com/media/1V1QBXR2OsStf3gyrC/giphy.gif",
        "https://media.giphy.com/media/jKBUIMSF9xTXtZI16r/giphy.gif",
        "https://media.giphy.com/media/xyGifqV1H4n9vrlNuC/giphy.gif",
        "https://media.giphy.com/media/tWf0HlPhLQbpIBrwOw/giphy.gif",
    ]
    img = choice(gifList)
    return img


def job(context):
    users = db.search_db()
    now_all = get_date()

    now_date, now_time = now_all.split()
    now_date = datetime.strptime(now_date, "%d.%m.%y")
    now_time = datetime.strptime(now_time, "%H:%M:%S")

    now_all_dateType = datetime.strptime(now_all, "%d.%m.%y %H:%M:%S")

    for i in users:
        try:
            date = i[0] + " " + i[1]
            date_dateType = datetime.strptime(date, "%d.%m.%y %H:%M:%S")

            if(date_dateType <= now_all_dateType):
                format_now_date = datetime.strftime(now_date, "%d.%m.%y")
                format_now_time = datetime.strftime(now_time, "%H:%M:%S")
                db.update_table_db(i[0], format_now_date, format_now_time)
                message, img = randDroch()
                updater.bot.send_animation(i[0], img, caption=message)

        except Unauthorized:
            db.delete_from_db(i[0])

def get_date():
    current_dt = datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d.%m.%y %H:%M:%S")
    return current_dt
#доделать прикол со стопом тип если уже не подписан отправить сообщение о том что он не подписан да
#можно и на вдс пустить
def stop(update: Update, context: CallbackContext):
    users = db.search_db()
    db.delete_from_db(update.effective_chat.id)
    context.bot.send_message(update._effective_chat.id, "Вы отписались от напоминалок")


def main() -> None:
    """Start the bot."""
    fapnow_handler = CommandHandler('fapnow', fapNow)
    stop_handler = CommandHandler('stop', stop)
    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(fapnow_handler)
    dispatcher.add_handler(stop_handler)


    updater.job_queue.run_repeating(job, 3600)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


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

#1460969666	18.04.22	19:54:27
