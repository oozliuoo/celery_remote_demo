
from celery import Celery

"""
Comment out this line if you want to test with RabbitMQ
"""
# app = Celery('tasks', backend='amqp', broker='amqp://<user>:<password>@<ip>/<vhost>')

"""
Comment out this line if you want to test with redis
"""
# app = Celery('tasks', backend='amqp',broker='redis://<ip>:<port>/<redisdb>')

@app.task(bind=True, track_started=True)
def add(self, x, y):
	return x + y