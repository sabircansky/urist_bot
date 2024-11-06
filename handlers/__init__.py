from aiogram import Router, F
from aiogram.filters import Command

from handlers.common import send_welcome, return_to_main_menu
from handlers.consultation import legal_consultation, ConsultationStates
from handlers.document_generation import (
    document_generation,
    # другие функции
)
from handlers.document_analysis import (
    document_analysis,
    # другие функции
)
from handlers.contact_lawyer import (
    contact_lawyer,
    # другие функции
)

router = Router()

# Команда /start
router.message.register(send_welcome, Command('start'))

# Вернуться в главное меню
router.message.register(return_to_main_menu, F.text == "Вернуться в главное меню")

# Юридическая консультация
router.message.register(legal_consultation, F.text == "Юридическая консультация")
# router.message.register(ConsultationStates.waiting_for_question)

# Генерация документов
router.message.register(document_generation, F.text == "Генерация документов")
# Регистрация других обработчиков генерации документов

# Анализ документов
router.message.register(document_analysis, F.text == "Анализ документов")
# Регистрация других обработчиков анализа документов

# Связаться с юристом
router.message.register(contact_lawyer, F.text == "Связаться с юристом")
# Регистрация других обработчиков связи с юристом

# Обработчик callback_query
# router.callback_query.register(process_callback)
