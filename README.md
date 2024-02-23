# PyFlame

The PyFlame Website is a robust Django Framework project aimed for gaining web development skills and developing reliable and secure applications. Including how to serve static files to add CSS, JavaScript and images. Implementing of Forms to accept user input and how to manage sessions to ensure a reliable user experience. Adding persisting data to a SQL database, of course an Admin user and the built-in Admin GUI to manage models.

## TODO

### Improve

- [ ] styling  
- [ ] ADD users profile view

### Completed

- [x] Upgrade protocol from HTTP to HTTPS
- [x] Add user Register and Authentication   
- [x] Add post comments




## test locally:
```
$ DJANGO_DB_ALIAS=development poetry run ./manage.py runserver

# run with debugger
$ DJANGO_DB_ALIAS=development poetry run gunicorn --reload flame.wsgi --keyfile private_key.pem --certfile certificate.pem 
```

