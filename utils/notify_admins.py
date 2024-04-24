import os
import logging

from aiogram import Dispatcher

ADMINS = os.getenv('ADMINS')


async def on_startup_notify(dp: Dispatcher):
    for admin in [6826658385, 5605407368]:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")

        except Exception as err:
            logging.exception(err)
