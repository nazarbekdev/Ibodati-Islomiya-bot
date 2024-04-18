import requests
from aiogram import types

from loader import dp


@dp.message_handler(commands=['user_count'])
async def user_count(message: types.Message):
    url_user_list = "http://127.0.0.1:8000/botuserlist"
    user_list = requests.get(url_user_list).json()
    await dp.bot.send_message(message.chat.id, f'<b><i><u><pre>Ibodati Islomiya</pre></u></i></b> Foydalanuvchilar soni: {len(user_list)}')

