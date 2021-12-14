from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv


from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

print(os.getenv('TOKEN'))

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
