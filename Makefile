run-redis:
	redis-server --daemonize yes

celery-beat:
	celery -A spiders.celery beat -l info

celery-worker:
	celery worker -l info -A remote

