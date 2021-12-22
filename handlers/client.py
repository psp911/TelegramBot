from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.types import ReplyKeyboardRemove


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
		await bot.send_message(message.from_user.id, "Привет {0.first_name} {0.last_name}".format(message.from_user))
		#await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС !!!, напишите ему:\nhttps://t.me/Pizza_Sheff_PspBot')


#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9 до 23')


#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Ул.Колбасная 15')


#@dp.register_message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение'])
	dp.register_message_handler(pizza_menu_command, commands=['Меню'])
