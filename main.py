# https://www.youtube.com/watch?v=yetfif4j_go&ab_channel=CodeWriter
# Как сделать меню для Телеграм бота на aiogram Python

import logging
from aiogram import Bot, Dispatcher, executor, types


import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

print (os.getenv('TOKEN'))

#TOKEN="2110783733:AAG6p8vQCYp6EPJrv9sjmvigJJbrWukR-yM"
TOKEN=os.getenv('TOKEN')

bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, "Привет {0.first_name} {0.last_name}".format(message.from_user))

@dp.message_handler()	
async def bot_message(message: types.Message):
	await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)

