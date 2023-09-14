from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = [
    [
        KeyboardButton(text='Рандом')]
    ]

kb_markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)