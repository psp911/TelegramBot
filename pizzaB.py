# https://www.youtube.com/watch?v=yetfif4j_go&ab_channel=CodeWriter
# Как сделать меню для Телеграм бота на aiogram Python

import logging
from aiogram import Bot, Dispatcher, executor, types



import markups as nav
import random

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

print (os.getenv('TOKEN'))

TOKEN=os.getenv('TOKEN')

bot=Bot(token=TOKEN)
dp=Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, "Привет {0.first_name} {0.last_name}".format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()	
async def bot_message(message: types.Message):
	#await bot.send_message(message.from_user.id, message.text)
	if message.text == 'Рандомное число':
		await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(1000,9999)))
	
	elif message.text == 'Главное Меню':
		await bot.send_message(message.from_user.id, 'Главное Меню',  reply_markup = nav.mainMenu)
	
	elif message.text == 'Другое':
		await bot.send_message(message.from_user.id, 'Другое',  reply_markup = nav.otherMenu)

	elif message.text == 'Информация':
		await bot.send_message(message.from_user.id, 'Информация')
	
	elif message.text == 'Курс валют':
		await bot.send_message(message.from_user.id, 'Курс валют')

	else:
		await message.reply('Неизвестная команда')

if __name__ == '__pizzaB__':
	executor.start_polling(dp, skip_updates = True)

