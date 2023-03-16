from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quez_2(call: types.CallbackQuery):
    question = 'Какая самая популярная игра за 2022 год?'
    answer = [
        'Destiny 2',
        'ARK: Survival Evolved',
        'Dota 2',
        'Counter Strike: Global Offensive',
        'Team Fortress 2',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Counter Strike: Global Offensive - 607 928',
    )


async def quez_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data='button_2')
    markup.add(button_1)
    question = 'в каком году написали питон?'
    answer = [
        '1990-1991',
        '1988-1990',
        '1899-1900',
        '1985-1986',
        '1989–1991 ',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        reply_markup=markup
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quez_2, text="button_1")
    dp.register_callback_query_handler(quez_3, text='button_2')