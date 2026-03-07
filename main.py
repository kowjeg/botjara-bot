import logging
import asyncio
from aiogram import Bot, Dispatcher

from handlers import router
from config import BOT_TOKEN


dp = Dispatcher()
logger = logging.getLogger(__name__)


dp.include_routers(router)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s")
asyncio.run(main())