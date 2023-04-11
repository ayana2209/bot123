from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from decouple import config
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Приветствую вас хозяин ♡＼(￣▽￣)／♡")


@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/Petrik pepett.jpeg', 'rb')
    await bot.send_photo(message.chat.id, photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1)

    question = "Самое высокое дерево?"
    answer = [
        "Дуб",
        "Гиперион",
        "Сосна",
        "Генерал Шерман",
        "Секвойя красная",
        "Ромашка",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Иди учись",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="quiz_1_button")
async def quiz_2(call: types.CallbackQuery):
    question = "На каком языке была написана игра марио?"
    answer = [
            'Java',
            'Python',
            'C++',
            'Assembly',
            'C#',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Иди учись",
        open_period=10,
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
