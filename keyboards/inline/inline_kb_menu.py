from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Освітні програми', callback_data='Кнопки4'),
            InlineKeyboardButton(text='Вступнику', callback_data='Вступнику')
        ],
        [
            InlineKeyboardButton(text='Подати заяву', url='https://docs.google.com/forms/d/e/1FAIpQLSe1MM86Fl_EtZBXO0K6_qLbPfCqbSrYjETNCGkHeqNJGwkwBQ/viewform?usp=sf_link')
        ],
        [
            InlineKeyboardButton(text='Зв’язатися з нами', callback_data='Кнопки3'),
            InlineKeyboardButton(text='Контакти', callback_data='Контакти')
        ]
    ]
)