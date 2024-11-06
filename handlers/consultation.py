from pprint import pprint

from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import dp
from keyboards.menus import main_menu
from keyboards.menus import back_to_main_menu
from utils.openai_helper import generate_openai_response_and_buttons

router = Router()


class ConsultationStates(StatesGroup):
    waiting_for_question = State()
    consultation = State()
    waiting_for_step = State()


async def legal_consultation(message: types.Message, state: FSMContext):
    await message.reply("Введите ваш запрос для консультации: ", reply_markup=back_to_main_menu)
    await state.set_state(ConsultationStates.consultation)


@dp.message(ConsultationStates.consultation)
async def handle_resp_text(message: types.Message, state: FSMContext):
    response = message.text
    if response == "Вернуться в главное меню":
        await state.clear()
        await message.reply(
            "Вы вернулись в главное меню. Выберите нужную опцию:",
            reply_markup=main_menu
        )
        return
    print(response)
    # Тут происходит отправление запроса в гпт
    answer, buttons_data = await generate_openai_response_and_buttons(response)
    # Создаем клавиатуру
    builder = InlineKeyboardBuilder()
    for button in buttons_data:
        builder.button(text=button['text'], callback_data=button['callback_data'])
    builder.adjust(1)  # Выравнивание по 1 кнопке в строке
    await message.reply(text=answer, reply_markup=builder.as_markup())
    await state.set_state(ConsultationStates.waiting_for_step)

# @dp.message(ConsultationStates.consultation)
# async def handle_resp_text(message: types.Message, state: FSMContext):
