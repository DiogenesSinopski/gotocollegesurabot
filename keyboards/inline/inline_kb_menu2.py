from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu2 = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Маркетинг', callback_data='Маркетинг')
        ],
        [
            InlineKeyboardButton(text='Облік і консалтинг', callback_data='Облік')
        ],
        [
            InlineKeyboardButton(text='Економіка', callback_data='Економіка')
        ]
    ]
)