from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Головне меню'),
            KeyboardButton(text='Як до нас дібратися'),
        ]
    ],
    resize_keyboard=True
)