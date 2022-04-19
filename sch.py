import asyncio
import aioschedule


async def noon_print():
    print("It's noon!")

async def scheduler():
    aioschedule.every(3).seconds.do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def sendAsync():
    loop = asyncio.get_event_loop()
    await loop.create_task(scheduler())
    await loop.run_forever()
sendAsync()

print("hello")
