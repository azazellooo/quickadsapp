# Adverts and announcements
(heroku link: http://quickadsapp.herokuapp.com/)

Для запуска проекта установите python версии 3.7 и выше, pip и virualenv

Поссле клонирования перейдите в склонированную папку и вывполните следующие команды:

Создайте виртуальное окружение командой
```bash
python3 -m virtualenv -p python3 venv
```

Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
```

Перейдите в папку hello:
```bash
cd hello
```

Установите зависимости командой

```bash
pip install -r requirements.txt
```

Примените миграции командой
```bash
./manage.py migrate
```

Загрузите фикстурные теги командой
```bash
./manage.py loaddata fixtures/tags.json
```

Загрузите группы и пользователей командой
```bash
./manage.py loaddata fixtures/auth.json
```


Загрузите фикстурные объявления командой
```bash
./manage.py loaddata fixtures/dump.json
```

Чтобы запустить сервер выполните:

```bash
./manage.py runserver
```

