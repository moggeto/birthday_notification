from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.types import Message

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='добавить')],
    [KeyboardButton(text='список')],
    [KeyboardButton(text='редактровать')]
], resize_keyboard=True, input_field_placeholder='menu')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='retarded gay party',
                          url=f'https://t.me/+k_Js9MiZrzxhZjQy')]
])
