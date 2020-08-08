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
