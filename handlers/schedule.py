import datetime

from aiogram import types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from config import bot


async def notification_id(message: types.Message):
    user_ids = [message.from_user.id]
    for user_id in user_ids:
        await message.answer(user_id[0], "Поздровляю, ты дожил до каникул ＼(￣▽￣)／!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    from datetime import datetime
    scheduler.add_job(
    notification_id,
        trigger=DateTrigger(
            run_date=datetime.datatime(year=2023, month=6, day=1, hour=8, minute=30)
        ),
        kwargs={"message": bot},
    )

    scheduler.start()