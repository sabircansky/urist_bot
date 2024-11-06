import logging
from config import OPENAI_API_KEY
from openai import OpenAI
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

client = OpenAI(api_key=OPENAI_API_KEY)


async def generate_openai_response_and_buttons(question):
    try:
        # Формируем промпт для OpenAI
        prompt = f"""
Вы выступаете в роли юридического консультанта по законодательству РФ.
Ответьте на вопрос пользователя кратко и по существу.
После ответа предложите три варианта дальнейших действий, которые могут быть полезны пользователю, в формате:

[Ответ]

Предложения:
1. [Текст кнопки 1]
2. [Текст кнопки 2]
3. [Текст кнопки 3]

Обратите внимание, что предложения должны быть релевантны ответу и полезны пользователю.
"""
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        assistant_reply = completion.choices[0].message.content.strip()

        # Разделяем ответ и предложения
        if "Предложения:" in assistant_reply:
            response_text, suggestions_text = assistant_reply.split("Предложения:", 1)
            response_text = response_text.strip()
            suggestions = suggestions_text.strip().split("\n")
            buttons = []
            for suggestion in suggestions:
                if suggestion.strip():
                    parts = suggestion.strip().split('.', 1)
                    if len(parts) == 2:
                        button_text = parts[1].strip()
                        buttons.append({'text': button_text, 'callback_data': f"action_{len(buttons)}"})
        else:
            response_text = assistant_reply
            buttons = []
    except Exception as e:
        logging.error(f"Ошибка при обращении к OpenAI API: {e}")
        response_text = "Извините, произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте позже."
        print(e)

    return [response_text, buttons]
