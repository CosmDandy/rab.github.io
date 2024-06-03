import logging

from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, WebAppInfo

from ..database.database_connection import client

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    result = client.query(f"SELECT COUNT(*) FROM go.Users WHERE User_tg_id = {message.from_user.id}")
    logging.info(result.result_rows)
    if result.result_rows[0][0] == 0:
        role_inline_kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text='Исполнитель', callback_data='1'),
                    types.InlineKeyboardButton(text='Заказчик', callback_data='0')
                ]
            ],
            resize_keyboard=True
        )
        # Send message with inline keyboard
        await message.answer('Выберите роль:', reply_markup=role_inline_kb)
    else:
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
        await message.answer(text='Please choose your role:', reply_markup=stock_inline_kb)


@router.message(Command('switch'))
async def switch_role_handler(message: Message) -> None:
    """
    Тут должна быть команда которая отправляет сообщение с кнопками для выбора роли и после меняет роль пользователя
    :param message:
    :return:
    """
    role_inline_kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Исполнитель', callback_data='1'),
                types.InlineKeyboardButton(text='Заказчик', callback_data='0')
            ]
        ],
        resize_keyboard=True
    )
    # Send message with inline keyboard
    await message.answer('Выберите роль:', reply_markup=role_inline_kb)


@router.message(Command('new_task'))
async def new_task(message: Message) -> None:
    # TODO document why this method is empty
    pass


@router.message(Command('stock'))
async def open_stock_handler(message: Message) -> None:
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
    await message.answer(text='Please choose your role:', reply_markup=stock_inline_kb)
