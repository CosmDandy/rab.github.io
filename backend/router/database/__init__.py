from aiogram import Router

from .database_connection import router as db_router

router = Router(name=__name__)

router.include_routers(db_router)
