import asyncio
import aioschedule
from random import randint, choice
import os

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



print(func())
