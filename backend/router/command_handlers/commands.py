import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from ..database.database_connection import client
from ..keyboards.keyboards import open_stock_inline_kb, user_init_roles_inline_kb, user_switch_roles_inline_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    result = client.query(f"SELECT COUNT(*) FROM go.Users WHERE User_tg_id = {message.from_user.id}")
    logging.info(result.result_rows[0][0])
    if result.result_rows[0][0] == 0:
        await message.answer('Выберите роль:', reply_markup=user_init_roles_inline_kb)
    else:
        await message.answer(text='Please choose your role:', reply_markup=open_stock_inline_kb)


@router.message(Command('switch'))
async def switch_role_handler(message: Message) -> None:
    """
    Тут должна быть команда которая отправляет сообщение с кнопками для выбора роли и после меняет роль пользователя
    :param message:
    :return:
    """
    await message.answer('Выберите роль:', reply_markup=user_switch_roles_inline_kb)


@router.message(Command('new_task'))
async def new_task(message: Message) -> None:
    # TODO document why this method is empty
    pass
