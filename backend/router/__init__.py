__all__ = ("router",)

from aiogram import Router

from .callback_handlers import router as main_callback_router
from .command_handlers import router as main_command_router
from .database import router as main_db_router

router = Router(name=__name__)

router.include_routers(
    main_callback_router,
    main_command_router,
    main_db_router
)
