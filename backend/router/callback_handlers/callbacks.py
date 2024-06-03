from datetime import datetime

from aiogram import F, Router, types

from ..database.database_connection import client
from ..keyboards.keyboards import open_stock_inline_kb, user_init_roles_data, user_switch_roles_data

router = Router(name=__name__)


@router.callback_query(lambda c: c.data in user_init_roles_data)
async def process_callback_switch_role(callback_query: types.CallbackQuery):
    # Get user role from callback data
    user_role = callback_query.data
    if user_role == user_init_roles_data[0]:
        user_role = 'Исполнитель'
        role = True
    else:
        user_role = 'Заказчик'
        role = False
    client.command(
        f"INSERT INTO go.Users (User_tg_id, User_registration_date, User_type, User_close_tasks, User_open_tasks, User_rating) VALUES ({callback_query.from_user.id}, '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', {role}, 0, 0, 5.0)")
    await callback_query.answer(text=f'Вы выбрали роль {user_role}', cache_time=5)
    await callback_query.message.edit_text(text='Please choose your role:', reply_markup=open_stock_inline_kb)


@router.callback_query(lambda c: c.data in user_switch_roles_data)
async def process_callback_switch_role(callback_query: types.CallbackQuery):
    # Get user role from callback data
    user_role = callback_query.data
    if user_role == user_switch_roles_data[0]:
        user_role = 'Исполнитель'
        role = True
    else:
        user_role = 'Заказчик'
        role = False
    # Here you can update the user's role in your database
    # For example:
    client.command(
        f"ALTER TABLE go.Users UPDATE User_type = '{role}' WHERE User_tg_id = {callback_query.from_user.id}")
    # Send a notification to the user about the role change
    await callback_query.answer(text=f'Вы выбрали роль {user_role}', chace_time=5)
