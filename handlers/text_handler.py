import logging

from aiogram import Router, F
from aiogram.types import Message

logger = logging.getLogger(__name__)
router = Router()


@router.message(F.text.lower() == 'привет')
async def hello_text(message: Message):
    await message.answer('и тебе привет')


@router.message(F.text.startswith('хочу'))
async def wanna_text(message: Message):
    await message.answer(f'хоти {message.text.removeprefix("хочу ")}' )

