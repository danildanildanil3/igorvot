import asyncio

from loguru import logger

from core.bot_app import start_bot


async def main():

    await start_bot()


if __name__ == "__main__":
    logger.info("Start main!")
    asyncio.run(main())

