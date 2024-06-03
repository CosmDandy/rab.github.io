from aiogram import Router

from .commands import router as command_router

router = Router(name=__name__)

router.include_routers(command_router)
