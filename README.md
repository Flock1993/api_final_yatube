# API для Yatube
Учебный проект 9 спринта курса **Яндекс.Практимум Python-разработчик**.
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://https://github.com/Flock1993/api_final_yatube.git
```
```
cd api_final_yatube

```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv

```

```
source venv/Scripts/activate

```

```
python -m pip install --upgrade pip

```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt

```

Выполнить миграции:

```
python manage.py makemigrations

```
```
python manage.py migrate

```

Запустить проект:

```
python manage.py runserver
```
## Примеры запросов к API:
```
GET http://127.0.0.1:8000/api/v1/posts/
Response:
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```
```
POST http://127.0.0.1:8000/api/v1/posts/
{
"text": "string",
"image": "string",
"group": 0
}
Response:
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
## Использованные технологии
Python 3.7, Django 2.2.16, Django Rest Framework 3.12.4, Djoser 2.1.0.
### Автор
Студент 35 когорты Python-разработки Строков Матвей
