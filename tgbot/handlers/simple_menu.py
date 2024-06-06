from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import as_section, as_key_value, as_marked_list
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from tgbot.keyboards.inline import simple_menu_keyboard, my_orders_keyboard, \
    OrderCallbackData
# from tgbot.keyboards.reply import another_menu
import tgbot.keyboards.reply as kb

menu_router = Router()


@menu_router.message(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Виберіть пункт меню:", reply_markup=kb.menu())
