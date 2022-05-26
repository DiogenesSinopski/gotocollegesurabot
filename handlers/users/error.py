from aiogram import types

from keyboards.inline import ikb_menu3
from loader import dp


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Зв’язатися з нами', reply_markup=ikb_menu3)
