# Ejemplo Flask Celery
Ejemplo Flask https://testdriven.io/courses/flask-celery/getting-started/

Debe tener instalado o corriendo Redis

```
docker run -d -p 6379:6379 redis
```

## Clone proyecto

```
https://github.com/fenavillarroel/flask_celery.git
```

Install dependencias

```
cd flask_celery
pip install -r requirements.txt
```

Run broker and backend

```
celery -A app.celery worker --loglevel=info
celery -A app.celery flower --port=5555
```

Run Flask App

```
flask --app app.py --debug run
```

