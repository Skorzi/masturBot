import asyncio
import aioschedule
from random import randint, choice
import os
import db
from datetime import datetime
import pytz

# async def noon_print():
#     print("It's noon!")

# async def scheduler():
#     aioschedule.every(3).seconds.do(noon_print)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# async def sendAsync():
#     loop = asyncio.get_event_loop()
#     await loop.create_task(scheduler())
#     await loop.run_forever()
# sendAsync()

def func():
    rand = randint(0, 100)
    if rand < 50:
        message = "NE DROCHIT` SEGONDYA"
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

    else:
        message = "DROCHI SEGODNYA"
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
    return message, img

def job():
    bug_fix_date = "22.04.22"
    bug_fix_time = "22:15:22"
    bug_fix_plus = bug_fix_date + " " + bug_fix_time
    bug_fix_all = datetime.strptime(bug_fix_plus, "%d.%m.%y %H:%M:%S")

    print(bug_fix_all)
    print(type(bug_fix_all))
    users = db.search_db()
    now_all = get_date()
    
    now_date, now_time = now_all.split()
    now_date = datetime.strptime(now_date, "%d.%m.%y")
    now_time = datetime.strptime(now_time, "%H:%M:%S")

    now_new_all = datetime.strptime(now_all, "%d.%m.%y %H:%M:%S")
    diff = now_new_all - bug_fix_all
    print(now_new_all)
    print(bug_fix_all)
    print(diff.days)
    diff = int(diff.days)
    print(diff)
    print(type(diff))
    

    if diff:
        print("fdfd")

    # for i in users:
    #     # date = datetime.strptime(i[1], "%d.%m.%y")
    #     # time = datetime.strptime(i[2], "%H:%M:%S")
    #     date = i[1] + " " + i[2]
    #     date_reg_user = datetime.strptime(date, "%d.%m.%y %H:%M:%S")

    #     if(diff):
    #         format_now_date = datetime.strftime(now_date, "%d.%m.%y")
    #         format_now_time = datetime.strftime(now_time, "%H:%M:%S")
    #         db.update_table_db(i[0], format_now_date, format_now_time)

def get_date():
    current_dt = datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d.%m.%y %H:%M:%S")
    return current_dt

job()