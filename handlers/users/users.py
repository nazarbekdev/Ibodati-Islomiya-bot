import requests
from aiogram import types
from loader import dp


@dp.message_handler(commands=['users'])
async def users(message: types.Message):
    url = 'http://127.0.0.1:8000/users'
    response = requests.get(url).json()
    user_list = str(f'Foydalanuvchilar soni: {len(response)}\n\n')
    for user in response:
        user_list += f"{user['name']}\n{user['created']}\n\n"
    await message.answer(user_list)
