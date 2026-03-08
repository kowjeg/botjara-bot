import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.menu_keyboards import menu_keyboard
from api.weather import get_temperature

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command('menu'))
async def menu_handler(message: Message):
    logger.info('открываем меню в чате с пользователем %s', message.from_user.id)
    keyboard = menu_keyboard()
    await message.answer('Главное меню:', reply_markup=keyboard)

@router.message(F.text == '⛅ Погода')
async def weather_handler(message: Message):
    logger.info('показываем погоду пользователю %s', message.from_user.id)
    temp = await get_temperature()
    if temp is None:
        await message.answer('Не удалось получить информацию о погоде')
    else:
        await message.answer(f'сейчас в Москве {temp} °C')


@router.message(F.text == '📰 Новости')
async def news_handler(message: Message):
    logger.info('показываем новости пользователю %s', message.from_user.id)
    await message.answer('Сегодня все хорошо')


@router.message(F.text == '⚙️ Настройки')
async def settings_handler(message: Message):
    logger.info('показываем подменю настроек пользователю %s', message.from_user.id)
    await message.answer('Настройки не реализованы')


@router.message(F.text == '✖️ Закрыть меню')
async def close_menu_handler(message: Message):
    logger.info('закрываем меню в чате у пользователя %s', message.from_user.id)
    await message.answer('Меню закрыто', reply_markup=ReplyKeyboardRemove())