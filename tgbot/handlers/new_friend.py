from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

add_router = Router()


class Addition(StatesGroup):
    name = State()
    date = State()


@add_router.message(F.text == 'Добавить друга')
async def add_friend(message: Message, state: FSMContext):
    await state.set_state(Addition.name)
    await message.answer('введите имя друга')


@add_router.message(Addition.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Addition.date)
    await message.answer('введите дату рождения в формате DD-MM')


@add_router.message(Addition.date)
async def add_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    # await state.set_state(Addition)
    data = await state.get_data()
    await message.answer(f'name {data["name"]}, date {data["date"]}')
    await state.clear()
