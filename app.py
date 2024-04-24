from aiogram import executor
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import requests
import random
from aiogram import types, Dispatcher
from datetime import datetime
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


async def send_message(dp: Dispatcher):
    today = datetime.now()
    try:
        url = 'http://172.234.196.220:8001/users'
        url1 = 'http://172.234.196.220:8001/datalist'
        users = requests.get(url).json()
        data = requests.get(url1).json()
        random_data = random.choice(data)
        msg = "<b><i><u><pre>Bir o'qib ko'ring</pre></u></i></b>\n"
        msg += f"-  {random_data['savol']}\n•  {random_data['javob']}"
        for user in [5605407368, 2097864798]:
            await dp.bot.send_message(user, msg)
    except Exception as e:
        await dp.bot.send_message('Serverda nosozlik...')


async def scheduler():
    schulduler = AsyncIOScheduler(timezone='Asia/Tashkent')
    schulduler.add_job(send_message, 'interval', minutes=1, args=[dp])
    schulduler.start()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
