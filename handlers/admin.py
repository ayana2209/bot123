from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(f"{message.from_user.first_name} братан кикнул"
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группу!")


async def game(message: types.Message):
    if message.text.startswith('game'):
        if message.chat.type != "private":
            if message.from_user.id not in ADMINS:
                await message.answer("YOU ARE NOT MY BOSS!")
            else:
                emoji_1 = ["🎲", "🎰", "⚽️", "🎳", "🏀", "🎯"]
                await bot.send_game(message.chat.id, emoji=choice(emoji_1))
        else:
            await message.answer("Пиши в группу!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix='!/')
    dp.register_message_handler(game, commands=["game"])
