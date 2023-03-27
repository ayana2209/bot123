import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def notification_id(message: types.Message):
    notice = [message.from_user.id]


async def sleep():
    global notice
    for id in notice:
        await bot.send_message(id, 'Поздровляю, ты дожил до выходных!')


async def set_scheduler():
    aioschedule.every().saturday.do(sleep)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(notice, commands=["notice"])

