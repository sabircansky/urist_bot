from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.menus import back_to_main_menu
from handlers.common import return_to_main_menu


class DocumentGenerationStates(StatesGroup):
    waiting_for_document_type = State()
    waiting_for_details = State()


async def document_generation(message: types.Message, state: FSMContext):
    await message.reply("Пожалуйста, выберите тип документа, который вы хотите сгенерировать.",
                        reply_markup=back_to_main_menu)
    await state.set_state(DocumentGenerationStates.waiting_for_document_type)

# Добавьте обработчики для получения типа документа и деталей
