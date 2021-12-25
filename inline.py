from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from dotenv import load_dotenv

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

print(os.getenv('TOKEN'))

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка', url='https://google.com')
x = []
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='ссылки')
async def url_commnd(message : types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)