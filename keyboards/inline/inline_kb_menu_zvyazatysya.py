from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_zvyazatysya = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Написати', url='https://t.me/sura_off'),
            InlineKeyboardButton(text='Подзвонити', callback_data='Подзвонити')
        ],
        [
            InlineKeyboardButton(text='Передзвонити', callback_data='112241')
        ]
    ]
)