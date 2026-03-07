from aiogram import Router
from .commands_handler import router as command_router
from .text_handler import router as text_router
from .fsm_handler import router as fsm_router

router = Router()
router.include_routers(command_router, text_router, fsm_router)