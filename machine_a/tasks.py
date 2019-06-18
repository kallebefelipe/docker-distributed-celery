from celery import task


@task
def add(x, y):
    print('machine a')
    print(x+y)
    return x + y
