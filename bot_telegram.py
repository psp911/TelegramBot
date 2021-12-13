# https://youtu.be/TYs3-uyjC30


import logging
from aiogram.utils import executor
from create_bot import dp







async def on_startup(_):
	print ('Бот вышел в онлайн')


from handlers import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True, on_startup=on_startup)


