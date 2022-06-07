# Запуск проекта
1.Клонировать репозиторий.
`git clone https://github.com/midnightrebel/test_task.git`

2.Создать и активировать виртуальное окружение.
```
- Windows
python -m venv venv
.\venv\Scripts\activate
- Linux
python3 -m venv venv
source venv/bin/activate/
```
3.Установить зависимости для проекта.
```
pip install -r r.txt
```
4.Зайти в папку application и применить миграции.
```
cd application
python manage.py migrate
```
5.Запустить сервер.
```
python manage.py runserver
```


