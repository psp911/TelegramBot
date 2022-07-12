
# Как добавить новую машину к Гитхабу - авторизация SSH
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys


# Клонировать репозиторий на новую машину 
git clone git@github.com:psp911/TelegramBot.git


# Создание виртуальной среды
python3 -m venv venv

# Активация виртуальной среды
source venv/bin/activate

# Деактивация виртуальной среды
(venv) netpoint@ubuntu:~/myapp$ deactivate

# Установка необходимых пакетов для работы программы
pip3 install -r requirements.txt


# Проиндексировать изменения
git add .

# Закоммитить
git commit -m "теперь снова работает ОТМЕНА"

# Отправить на сервер
git push