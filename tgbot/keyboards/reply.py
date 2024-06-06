from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu():
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text='Добавить друга')
    keyboard.button(text='Редактировать')
    keyboard.button(text='Уведомления')
    keyboard.button(text='Настройки')

    return keyboard.adjust(3, 2).as_markup()


def add_friend():
    pass


def see_all():
    pass


def settings():
    pass
