from datetime import datetime

from aiogram import Router, types
from aiogram.types import WebAppInfo

from ..database.database_connection import client

router = Router(name=__name__)


@router.callback_query(lambda c: c.data in ['0', '1'])
async def process_callback_switch_role(callback_query: types.CallbackQuery):
    # Get user role from callback data
    user_role = callback_query.data
    if user_role == '1':
        user_role = 'Исполнитель'
        role = True
    else:
        user_role = 'Заказчик'
        role = False
    client.command(
        f"INSERT INTO go.Users (User_tg_id, User_registration_date, User_type, User_close_tasks, User_open_tasks, User_rating) VALUES ({callback_query.from_user.id}, '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', {role}, 0, 0, 5.0)")
    # Here you can update the user's role in your database
    # For example:
    # Send a notification to the user about the role change
    await callback_query.answer(text=f'Вы выбрали роль {user_role}', cache_time=5)
    stock_inline_kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Открыть биржу', web_app=WebAppInfo(
                    url='https://cosmdandy.github.io/rab.github.io/frontend/index.html'))
            ]
        ],
        resize_keyboard=True
    )
    # Send message with inline keyboard
    await callback_query.message.edit_text(text='Please choose your role:', reply_markup=stock_inline_kb)


@router.callback_query(lambda c: c.data in ['0', '1'])
async def process_callback_switch_role(callback_query: types.CallbackQuery):
    # Get user role from callback data
    user_role = callback_query.data
    if user_role == '1':
        user_role = 'Исполнитель'
    else:
        user_role = 'Заказчик'
    # Here you can update the user's role in your database
    # For example:
    await client.execute(
        f"UPDATE go.Users SET User_type = '{user_role}' WHERE User_tg_id = {callback_query.from_user.id}")
    # Send a notification to the user about the role change
    await callback_query.answer(text=f'Вы выбрали роль {user_role}', chace_time=5)
