
from celery import Celery

app = Celery('tasks', backend='amqp',
broker='amqp://root:Chuangyizhi2013,@139.162.118.6/test')

@app.task(bind=True, track_started=True)
def add(self, x, y):
	return x + y