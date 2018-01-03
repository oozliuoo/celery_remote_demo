# Send Celery Tasks to another machine


Note: Make sure you are in python 3.6, you could follow [this post](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04) to install conda and manage your environment properly

## Using Celery & RabbitMQ to demo.

### On Machine A:

1. Install Celery & RabbitMQ.
2. Clone this repository and update the `username`, `password`, `ip` and `vhost` as you need.
3. Configure RabbitMQ so that Machine B can connect to it.

~~~bash
# add new user
sudo rabbitmqctl add_user <user> <password>

# add new virtual host
sudo rabbitmqctl add_vhost <vhost_name>

# set permissions for user on vhost
sudo rabbitmqctl set_permissions -p <vhost_name> <user> ".*" ".*" ".*"

# restart rabbit
sudo rabbitmqctl restart
~~~

4. In your python3.6 environment, launch the python console and do:

~~~python
from remote import add

a = add.delay(3, 3)
~~~

### On Machine B

1. Install Celery
2. Clone this repository and update the `username`, `password`, `ip` and `vhost` as you need.
3. Run the worker

~~~bash
celery worker -l info -A remote
~~~

As soon as you run the above command, you should see the worker received tasks and executed. And if you go back to machineA, and check `a.status` and `a.result`, you should see that task is finished and result is returned.

## Using Celery & Redis

### On Machine A:

1. Install Celery & RabbitMQ.
2. Clone this repository and update the `ip`, `port` and `redisdb` as you need.
3. Install `redis` and configure it properly as covered [here](https://redis.io/topics/quickstart)
4. Enter your python3.6 environment, install redis by running `pip install redis`
5. In your python3.6 environment, launch the python console and do:

~~~python
from remote import add

a = add.delay(3, 3)
~~~

### On Machine B

1. Install Celery
2. Clone this repository and update the `username`, `password`, `ip` and `vhost` as you need.
3. Enter your python3.6 environment, install redis by running `pip install redis`
4. Run the worker

As soon as you run the above command, you should see the worker received tasks and executed. And if you go back to machineA, and check `a.status` and `a.result`, you should see that task is finished and result is returned.