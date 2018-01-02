
from celery import Celery

app = Celery('tasks', backend='amqp',
broker='amqp:///root:Chuangyizhi2013,@139.162.105.73')

@app.task
def add(x, y):
	return x + y