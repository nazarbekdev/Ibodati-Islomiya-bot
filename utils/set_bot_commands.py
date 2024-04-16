from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("book", "Ibodati Islomiya kitobi"),
            types.BotCommand("search", "savol bo'yicha izlash"),
        ]
    )
