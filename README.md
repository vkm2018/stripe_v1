

Запустить локольно:

1. Клонирование:
``` 
mkdir stripe_service
cd stripe_service
git clone <SSH repo_url>
```

2. Зависимости
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Создать БД
4. Необходимо создать .env и по аналогии .env.example заполнить параметры подключений

5. Сделать миграции и создать супер пользователя

```
./manage.py migrate
./manage.py createsuperuser
```
6. Запустить сервер

```
./manage.py runserver
```