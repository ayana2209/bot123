from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def start_command(message: types.Message):
    await message.answer('Hello!')


async def mem(message: types.Message):
    photo = open('media/654.jpeg', 'rb')
    await bot.send_photo(message.chat.id, photo)


async def pin(message: types.Message):
    if message.chat.type != "private":
        if not message.reply_to_message:
            await message.answer("Какое сообщение хотите закрепить?")
        elif message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


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


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="!/")
    dp.register_message_handler(quiz_1, commands=['quiz'])