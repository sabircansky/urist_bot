import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

OPENAI_API_KEY = ""
API_TOKEN = ""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
