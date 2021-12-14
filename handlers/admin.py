from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class FSMAdmin(StateGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#Начало диалога загрузки нового пункта меню
@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message)
    await FSMAdmin.photo.set()

# Продолжение тут - https://youtu.be/nF1p1JjuR3U?t=602



