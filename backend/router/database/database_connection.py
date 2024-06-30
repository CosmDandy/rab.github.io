from os import getenv

import clickhouse_connect
from aiogram import Router
from aiogram.types import WebAppInfo

router = Router(name=__name__)

client = clickhouse_connect.get_client(host='clickhouse', port=8123, username=getenv('CLICKHOUSE_USER'),
                                       password=getenv('CLICKHOUSE_PASSWORD'), database='go')

web_app = WebAppInfo(url='https://cosmdandy.github.io/rab.github.io/frontend/index.html')

@router.message( )
async def get_web_app(message):
    await message.answer(text='Here is the link to the web app:', reply_markup=web_app)