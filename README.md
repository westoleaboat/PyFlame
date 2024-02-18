# PyFlame

run locally:
```
DJANGO_DB_ALIAS=development poetry run ./manage.py runserver

#run with debugger
DJANGO_DB_ALIAS=development poetry run gunicorn --reload flame.wsgi --keyfile private_key.pem --certfile certificate.pem 
```