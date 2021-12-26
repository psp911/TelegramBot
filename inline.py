from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
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

answ = dict()

# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка', url='https://google.com')
x = []
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='ссылки')
async def url_commnd(message : types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Не Like', callback_data='like_-1'))

@dp.message_handler(commands='test')
async def test_commands(message : types.Message):
    await message.answer('За мир во всем мире', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    print(res)
    print(answ)
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)





if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)