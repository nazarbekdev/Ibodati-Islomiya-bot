from datetime import datetime
import logging
import requests
from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNEL
from keyboards.inline.subscriptions import check_button
from loader import dp, bot
from utils.misc import subscription

logging.basicConfig(level=logging.INFO)

url = "http://127.0.0.1:8000/botuser"
url_user_list = "http://127.0.0.1:8000/botuserlist"
time = str(datetime.now())

user_list = requests.get(url_user_list).json()


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    try:
        channels_format = str()
        user_list = requests.get(url_user_list).json()
        if message.from_user.id not in user_list:
            requests.post(url, data={'name': message.from_user.full_name, 'user_id': int(message.from_user.id), 'created': time[:16]})

        for channel in CHANNEL:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            channels_format += f"✅ <a href='{invite_link}'>{chat.title}</a>\n"

        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nSizni ko'rib turganimizdan xursandmiz 😊\n\n"
                             f"Botdan foydalanish uchun, 👇 quyidagi kanallarga obuna bo'ling:\n\n"
                             f"{channels_format}",
                             reply_markup=check_button, disable_web_page_preview=True)
    except Exception as e:
        logging.exception("An error occurred: %s", str(e))


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNEL:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            invite_link = await channel.export_invite_link()
            result += f"✅ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanallarga obuna bo'lmagansiz! "
                       f"<a href='{invite_link}'> Obuna bo'ling!</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)
