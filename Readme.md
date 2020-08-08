## Steps to run server

install required libraries from requirements.txt

pip3 install -r requirements.txt

apt-get install -y erlang

apt-get install rabbitmq-server

systemctl enable rabbitmq-server

systemctl start rabbitmq-server

### Run these commands in saperate terminal

python3 manage.py runserver

celery -A mysite worker -l info

celery -A my_app beat -l info

![alt text](https://github.com/Gr8ayu/Django_celery_rabbitMQ/blob/master/images/Screenshot%20from%202020-08-08%2006-01-51.png?raw=true)

![alt text](https://github.com/Gr8ayu/Django_celery_rabbitMQ/blob/master/images/Screenshot%20from%202020-08-08%2006-02-35.png?raw=true)

![alt text](https://github.com/Gr8ayu/Django_celery_rabbitMQ/blob/master/images/Screenshot%20from%202020-08-08%2006-04-12.png?raw=true)
