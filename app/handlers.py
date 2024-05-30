from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
import app.keyboards as kb

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f'привет {message.from_user.first_name}\n это твой айди {message.from_user.id}', reply_markup=kb.main)


@router.message(Command('help'))
async def help(message: Message):
    await message.answer('Команда help')


