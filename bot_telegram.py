# https://youtu.be/TYs3-uyjC30
# Telegram бот на python aiogram #1 разработка бота с нуля

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



@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита')
		await bot.send_message(message.from_user.id, "Привет {0.first_name} {0.last_name}".format(message.from_user), reply_markup = nav.mainMenu)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_Sheff_PspBot')



@dp.message_handler()
async def command_start(message : types.Message):
	try:
		if message.text == "Привет":
			await message.answer('И тебе привет!')
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_Sheff_PspBot')



@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9 до 23')




#'*********Админская часть **********





#'*********Общая часть **********





#@dp.message_handler()
#async def echo_send(message : types.Message):
	#await message.answer(message.text)
	#await message.reply(message.text)
#	await bot.send_message(message.from_user.id, message.text)






if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)


