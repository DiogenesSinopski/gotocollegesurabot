from aiogram import types
from aiogram.types import CallbackQuery, Message, InputFile
from keyboards.inline import ikb_menu, ikb_menu4, ikb_menu3, ikb_menu2
from loader import dp

@dp.message_handler(text='Головне меню')
async def show_inline_menu(message: types.Message):
    await message.answer('''Що вміє цей бот?
Бот Фахового коледжу СУРА (м. Черкаси) дозволяє:
- Зв’язатися з нашим консультантом;
- Дізнатися про спеціальності та освітні програми;
- Подати заявку на вступ;
- Запросити про допомогу зі вступу, реєстрації on-line кабінету вступника;
- Дізнатися розпорядок роботи приймальної комісії.

Оберіть що вас цікавить''', reply_markup=ikb_menu)

@dp.message_handler(text='Як до нас дібратися')
async def menu_index(message: types.Message):
    await message.answer_location(latitude=49.40548059551326, longitude=32.05391222883521)

@dp.callback_query_handler(text='Вступнику')
async def send_message(call: CallbackQuery):
    await call.message.answer('''Розпорядок роботи приймальної комісії
понеділок – п’ятниця з 10.00 до 14.00''')

@dp.callback_query_handler(text='Контакти')
async def send_message(call: CallbackQuery):
    await call.message.answer('''
вул. Нечуя-Левицького, 16
м. Черкаси, 18028, Україна
Телефон: (0472) 64-70-55
Телефон приймальної комісії:
(099) 105-27-71, (098) 340-10-36,
(063) 799-42-51
Університет: rauniver@suem.edu.ua
Коледж: college@suem.edu.ua''')

@dp.callback_query_handler(text='Діджитал')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)

@dp.callback_query_handler(text='Кнопки4')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu4)

@dp.callback_query_handler(text='Кнопки3')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu3)

@dp.callback_query_handler(text='Економіка')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Digital_econom.jpg'))

@dp.callback_query_handler(text='Маркетинг')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Digital_market.jpg'))

@dp.callback_query_handler(text='Облік')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Digital_econom.jpg'))


@dp.callback_query_handler(text='авто')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Avto.jpg'))


@dp.callback_query_handler(text='Док адміністрування')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Docum_admin.jpg'))


@dp.callback_query_handler(text='Право')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Pravo.jpg'))

@dp.callback_query_handler(text='Туризм')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Turyzm.jpg'))


@dp.callback_query_handler(text='dcnfg')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_contact(phone_number='+380991052771', first_name='СУЕМ')

