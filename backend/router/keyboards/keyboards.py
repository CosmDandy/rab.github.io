from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

user_init_roles_data = ['user_init_roles_1', 'user_init_roles_0']
user_init_roles_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Исполнитель', callback_data=user_init_roles_data[0]),
            InlineKeyboardButton(text='Заказчик', callback_data=user_init_roles_data[1])
        ]
    ],
    resize_keyboard=True
)

user_switch_roles_data = ['user_switch_roles_1', 'user_switch_roles_0']
user_switch_roles_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Исполнитель', callback_data=user_switch_roles_data[0]),
            InlineKeyboardButton(text='Заказчик', callback_data=user_switch_roles_data[1])
        ]
    ],
    resize_keyboard=True
)

open_stock_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Открыть биржу', web_app=WebAppInfo(
                url='https://cosmdandy.github.io/rab.github.io/frontend/index.html'))
        ],
        [
            InlineKeyboardButton(text='Подписаться на канал',
                                 url='https://t.me/go_4work')
        ]
    ],
    resize_keyboard=True
)

web_app = WebAppInfo(url='https://cosmdandy.github.io/rab.github.io/frontend/index.html')

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Site", web_app=web_app)]
])
