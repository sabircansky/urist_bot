from aiogram import types
from aiogram.fsm.context import FSMContext

from keyboards.menus import back_to_main_menu


async def contact_lawyer(message: types.Message, state: FSMContext):
    await message.reply(
        "Для связи с юристом, пожалуйста, позвоните по номеру +7 (123) 456-78-90 или напишите на email example@example.com.",
        reply_markup=back_to_main_menu)
