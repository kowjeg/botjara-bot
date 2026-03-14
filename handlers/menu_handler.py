import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.menu_keyboards import menu_keyboard, weather_get_location
from keyboards.inline_keyboards import demo_inline
from api.weather import get_temperature
from states.states import WeatherState

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command('menu'))
async def menu_handler(message: Message):
    logger.info('открываем меню в чате с пользователем %s', message.from_user.id)
    keyboard = menu_keyboard()
    await message.answer('Главное меню:', reply_markup=keyboard)

@router.message(F.text == '⛅ Погода')
async def weather_start(message: Message, state: FSMContext):
    logger.info('показываем погоду пользователю %s', message.from_user.id)
    await state.set_state(WeatherState.waiting_location)
    await message.answer('Отправьте геолокацию для определения температуры по ней', reply_markup=weather_get_location())

@router.message(WeatherState.waiting_location, F.location)
async def weather_handler(message: Message, state: FSMContext):
    await state.clear()
    lat = message.location.latitude
    lon = message.location.longitude
    temp = await get_temperature(lat, lon)
    if temp is None:
        await message.answer('Не удалось получить информацию о погоде', reply_markup=menu_keyboard())
    else:
        await message.answer(f'Погода по вашей геолокации сейчас {temp} °C', reply_markup=menu_keyboard())


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


@router.message(Command('inline_menu'))
async def inline_menu_handler(message: Message) -> None:
    logger.info('Пользователь %s вызвал inline меню %s', message.from_user.id, message.text)
    await message.answer('Inline версия меню', reply_markup=demo_inline())




