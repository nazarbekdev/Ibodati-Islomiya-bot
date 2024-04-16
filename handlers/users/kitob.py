from aiogram import types

from loader import dp


@dp.message_handler(commands=["book"])
async def kitob(message: types.Message):
    file_path = '/home/nazarbek/Portfolio/Ibodati_Islomiya_bot/document/IBODATI ISLOMIYA'
    with open(file_path, 'rb') as file:
        await dp.bot.send_document(message.chat.id, file)
