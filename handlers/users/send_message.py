import requests
import random
from aiogram import types, Dispatcher
from datetime import datetime

import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def send_message(dp: Dispatcher):
    today = datetime.now()
    try:
        url = 'http://127.0.0.1:8000/users'
        url1 = 'http://127.0.0.1:8000/datalist'
        users = requests.get(url).json()
        data = requests.get(url1).json()
        random_data = random.choice(data)
        msg = "<b><i><u><pre>Bir o'qib ko'ring</pre></u></i></b>\n"
        msg += f"-  {random_data['savol']}\n•  {random_data['javob']}"
        for user in users:
            await dp.bot.send_message(user, msg)
    except Exception as e:
        await dp.bot.send_message('Serverda nosozlik...')


async def scheduler():
    schulduler = AsyncIOScheduler(timezone='Asia/Tashkent')
    schulduler.add_job(send_message, 'interval', hour=6)
    schulduler.start()
    await asyncio.sleep(1)
