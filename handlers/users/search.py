import time

import requests
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loader import dp


# @dp.message_handler(CommandStart())
# async def answer_result(message: types.Message):
#     res_num = ['/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9']
#     if message.text[:2] in res_num:
#         await message.reply(message.text)
#

# Echo bot
@dp.message_handler(commands=["search"])
async def search_understand(message: types.Message):
    await message.answer("❌ Quyidagicha qidirish xato: Nafl namoz qanday o'qiladi?\n"
                         "✅ Savolni kalit soʻzlari bilan qidiring: 'Din nima', "
                         "  'Qazo namoz',  'Tahorat',  'Farz',  'Amal', ...")


@dp.message_handler()
async def search(message: types.Message):
    msg = message.text
    res_num = ['/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9']

    if msg[:2] not in res_num:
        result = str()
        url = f'http://127.0.0.1:8000/search?savol={msg}'
        response = requests.get(url).json()
        if response:
            for i in response:
                result += (f"-  <b><i>{i['savol']}</i></b>\n•  {i['javob'][:50]}...\n"
                           f"/{i['savol_id']}\n\n")
            time.sleep(1)
            await message.reply(result)
        else:
            await message.reply('Natija yoq')
    else:
        savol_id = int(msg[1:])
        url = f'http://127.0.0.1:8000/getdata/{savol_id}'
        response = requests.get(url).json()
        if requests.get(url).status_code == 200:
            await message.answer(f"- <b><i>{response['savol']}</i></b>\n• {response['javob']}\n\n"
                                 f"📗  {response['qism']} / {response['bolim']}\n"
                                 f"🕒  {response['created_at'][:10]}")
        else:
            await message.answer('Serverda xatolik 🤷‍♂️')
