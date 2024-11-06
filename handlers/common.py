from aiogram import types
from keyboards.menus import main_menu
from aiogram.fsm.context import FSMContext


async def send_welcome(message: types.Message):
    await message.reply(
        "Добро пожаловать! Я ваш юридический консультант. Выберите нужную опцию:",
        reply_markup=main_menu
    )


async def return_to_main_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Вы вернулись в главное меню. Выберите нужную опцию:",
        reply_markup=main_menu
    )
