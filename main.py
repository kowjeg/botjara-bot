import logging
import asyncio
from aiogram import Bot, Dispatcher

from handlers import router
from config import BOT_TOKEN
from api.weather import client

dp = Dispatcher()


@dp.shutdown()
async def on_shutdown():
    await client.aclose()


async def main():


    dp.include_routers(router)
    bot = Bot(token=BOT_TOKEN)
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s")
    logger = logging.getLogger(__name__)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

