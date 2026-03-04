from config import BOT_TOKEN


import asyncio
import logging

from aiogram import Bot, Dispatcher, html
from aiogram.filters import Command
from aiogram.types import Message


dp = Dispatcher()
logger = logging.getLogger("bot")

@dp.message()
async def start_handler(message: Message) -> None:

    logger.info(f'пришло сообщение от {message.chat.id} с текстом {message.text}')
    await message.send_copy(chat_id=message.chat.id)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())
