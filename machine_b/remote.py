from celery import Celery
from database.connection import get_process
from bots.piaui import ThemisconsultPi

# app = Celery(
#     'tasks', backend='amqp',
#     broker='amqp://<user>:<password>@<ip>/<vhost>')

# app = Celery(
#     'tasks', backend='amqp',
#     broker='amqp://172.16.103.250/6379')

# app = Celery(
#     'tasks', backend='amqp',
#     broker='redis://localhost:6379/0')

app = Celery(
    'tasks', backend='amqp',
    broker='redis://192.168.18.15:6379')

# app = Celery(
#     'tasks', backend='amqp',
#     broker='redis://redis:6379')

def trat_process(processos):
    for processo in processos:
        processo['_id'] = str(processo['_id'])
    return processos

@app.task
def run_extracao_task(collection, processos):
    processos = get_process(collection)
    processos = trat_process(processos)

    spider = ThemisconsultPi()
    spider.run(processos, collection)
