from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello!')


@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/654.jpeg', 'rb')
    await bot.send_photo(message.chat.id, photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data='button_1')
    markup.add(button_1)
    question = "Какая самая дорогая игровая компания в мире за 2023 год"
    answer = [
        'Activision Blizzard ',
        'Roblox Corp',
        'Electronic Arts '
        'Square Enix',
        'Unisoft',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Roblox Corp - доход $62 млрд',
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_1')
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


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
