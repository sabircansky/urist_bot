from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Юридическая консультация")],
        [KeyboardButton(text="Генерация документов")],
        [KeyboardButton(text="Анализ документов")],
        [KeyboardButton(text="Связаться с юристом")]
    ],
    resize_keyboard=True
)

# Кнопка для возврата в главное меню
back_to_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться в главное меню")]
    ],
    resize_keyboard=True
)
