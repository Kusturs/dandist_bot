import os
import asyncio
import logging
import sys

from dotenv import load_dotenv

from app.handlers import router
from app.database.models import async_main

from aiogram import Bot, Dispatcher


async def main():
	await async_main()
	load_dotenv()
	bot = Bot(token = os.getenv('TOKEN'))
	dp = Dispatcher()
	dp.include_router(router)
	await dp.start_polling(bot)


if __name__ == '__main__':
	try:
		logging.basicConfig(level = logging.INFO, stream = sys.stdout)
		asyncio.run(main())
	except KeyboardInterrupt:
		print('invalid')
