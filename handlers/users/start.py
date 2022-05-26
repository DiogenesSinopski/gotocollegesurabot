from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp

from filters import IsPrivate
from utils.misc import rate_limit


"""@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Твой айди: {message.from_user.id}')"""


@dp.message_handler(text='/start')
async def menu(message: types.Message):
    await message.answer(f'Привіт {message.from_user.full_name}!', reply_markup=kb_menu)