from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.menus import back_to_main_menu
from handlers.common import return_to_main_menu


class DocumentAnalysisStates(StatesGroup):
    waiting_for_document = State()


async def document_analysis(message: types.Message, state: FSMContext):
    await message.reply("Пожалуйста, отправьте документ для анализа.", reply_markup=back_to_main_menu)
    await state.set_state(DocumentAnalysisStates.waiting_for_document)

# Добавьте обработчики для получения документа и его обработки
