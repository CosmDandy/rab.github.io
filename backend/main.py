import sys

import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties

from aiogram.enums import ParseMode
from os import getenv
from router import router as main_router

TOKEN = getenv('BOT_TOKEN')


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
