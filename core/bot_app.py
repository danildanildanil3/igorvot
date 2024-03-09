from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger

from core.service import chat_spam
from core.settings.config import settings

bot = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

aioscheduler = AsyncIOScheduler()


async def start_bot():

    logger.info('Starting...')
    aioscheduler.add_job(
        func=chat_spam,
        args=[bot],
        trigger='interval',
        hours=settings.HOURS_TIMEOUT,
        minutes=settings.MINUTES_TIMEOUT,
        seconds=settings.SECONDS_TIMEOUT
    )
    aioscheduler.start()
    logger.info('Adding jobs and start spamming.')

    logger.info("Start polling")
    await dp.start_polling(bot)

