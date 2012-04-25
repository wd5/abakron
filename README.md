# Абакрон

Web-комикс от [D.Van](http://dvan.helloacy.ru), создателя [HelloACY](http://helloacy.ru) и [Pineapple Peak](http://pineapplepeak.blogspot.com).

Так как открытие сайта сильно затянулось по техническим причинам, было принято стратегическое решение начать делать его с нуля.

В качестве мотивирующего к продолжению разработки фактора было решено исходники выложить в публичный доступ.
Вы можете присоединиться к работе, если хотите.

## Установка 

1. Клонирование репозитория

    `git clone git://github.com/svartalf/abakron.git`

2. Создание виртуального окружения (виртуальные окружения — это клево!)

    `virtualenv .env`

3. Установка зависимостей

    `.env/bin/pip install -r requirements.txt`


4. Создание файла с локальными настройками проекта

    `touch settings_local.py`

5. Шаблон настроек

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Может быть любой db.backend
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
        }
    }

    SECRET_KEY = 'some-random-text-with-letters-digits-and-punctuation-symbols'
    ```

6. Структура базы данных

    ```
    .env/bin/python manage.py syncdb
    .env/bin/python manage.py migrate
    ```
