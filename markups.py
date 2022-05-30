# https://www.youtube.com/watch?v=yetfif4j_go&ab_channel=CodeWriter
# Как сделать меню для Телеграм бота на aiogram Python

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMine = KeyboardButton('Главное меню')


# ---- MAIN MeNU ------
btnRandom = KeyboardButton('Рандомное число')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)

#  ==Создать тренировку==   ==Редактировать тренировку==
#
#  Создать тренировку: Анонс, Дата, Время, Локация, Участники
#
#  Редактировать тренировку: Анонс, Дату, Время, Локация, Участники, Удалить тренировку

# ---- Other MeNU ------
btnInfo = KeyboardButton('Информация')
btnMoney = KeyboardButton('Курс валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo,btnMoney, btnMine)



