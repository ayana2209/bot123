from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("ТЫ НЕ МОЙ БОСС!")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer_photo(
                photo=user[-1],
                caption=f"{user[0]} {user[1]} {user[2]} {user[3]}\n"
                        f"@{user[4]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"DELETE {user[2]}",
                                         callback_data=f"DELETE {user[0]}")
                )
            )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("DELETE ", ""))
    await call.answer(text="УДАЛЕНО!", show_alert=True)
    await call.message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix='!/')
    dp.register_message_handler(game, commands=["game"])
    dp.register_message_handler(delete_data, commands=["del"])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("DELETE "))
