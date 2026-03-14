import logging
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

router = Router()
logger = logging.getLogger(__name__)

@router.callback_query(F.data == 'btn:news_btn')
async def inline_weather_handler(callback_query: CallbackQuery):
    logger.info('Пользователь %s нажал на inline кнопку %s', callback_query.from_user.id, callback_query.data)
    await callback_query.answer()
    await callback_query.message.answer('test')
