web: gunicorn config.wsgi:application
worker: newrelic-admin run-program celery worker --app=abo.taskapp --loglevel=info
