from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_osvitni = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Digital_маркетинг', callback_data='Маркетинг'),
            InlineKeyboardButton(text='Digital_облік', callback_data='Облік'),
        ],
        [
            InlineKeyboardButton(text='Digital_економіка', callback_data='Економіка'),
            InlineKeyboardButton(text='Право', callback_data='Право')
        ],
        [
            InlineKeyboardButton(text='Авто_транспорт', callback_data='авто'),
            InlineKeyboardButton(text='Туризм', callback_data='Туризм')
        ],
        [
            InlineKeyboardButton(text='Док_адміністрування', callback_data='Док адміністрування')
        ]
    ]
)