from celery import Celery

# app = Celery(
#     'tasks', backend='amqp',
#     broker='amqp://<user>:<password>@<ip>/<vhost>')

app = Celery(
    'tasks', backend='amqp',
    broker='redis://localhost:6379')


@app.task
def add(x, y):
    print('machine B')
    print(x+y)
    return x + y
