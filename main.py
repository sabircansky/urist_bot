import asyncio
import logging

# from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import API_TOKEN, dp, bot
from middlewares.logging_middleware import LoggingMiddleware
from handlers import router


async def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        filename='bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Инициализация бота и диспетчера
    # Подключение middleware
    dp.update.middleware(LoggingMiddleware())

    # Подключение роутеров
    dp.include_router(router)

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
