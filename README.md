# PyFlame

run locally:
```
DJANGO_DB_ALIAS=development poetry run ./manage.py runserver

DJANGO_DB_ALIAS=development poetry run gunicorn flame.wsgi --keyfile private_key.pem --certfile certificate.pem 
```