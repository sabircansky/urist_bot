import logging
from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            user = event.from_user
            logging.info(f"User: {user.id} - {user.full_name} - Message: {event.text}")
        return await handler(event, data)
