from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu():
    buttons = [
        [
            KeyboardButton(text='Добавить друга'),
            KeyboardButton(text='Редактировать')
        ],
        [
            KeyboardButton(text='Уведомления'),
            KeyboardButton(text='Настройки')
        ]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def another_menu():
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text='Добавить друга')
    keyboard.button(text='Редактировать')
    keyboard.button(text='Уведомления')
    keyboard.button(text='Настройки')

    keyboard.adjust(3, 1)
    return keyboard.as_markup()
