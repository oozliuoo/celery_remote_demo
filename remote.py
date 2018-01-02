
from celery import Celery

app = Celery('tasks', backend='amqp',
broker='amqp:///root:Chuangyizhi2013,@139.162.118.6')

@app.task
def add(x, y):
	return x + y