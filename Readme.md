## Background: 

Let’s build a product that provides an efficient backend to serve web dashboard for analysing calls and conversation and providing smart suggestions helping the sales team to learn and grow. 

## Assignment Details: 
```
In this assignment, you will be implementing the following using Django 
Create two models as follows:-
Task -> task should have task_type(integer) and task_desc(string)
TaskTracker -> tracker should have task_type(type of task to track), update_type(per day, weekly or monthly) and email
 Create apis to create and update tasks, task types can be pre-defined(let's say 1,2,3 and 4). Throw error if task type is not valid
Create api to create TaskTracker.
Create a background task using django-celery which should send email updates to users based on TaskTracker objects.  See example below

Ex:-  Let’s say I created a TaskTracker to track task of task_type = 4 and update_type = weekly. Now whenever someone creates a task of task_type = 4 it should send a consolidated update every monday(see update_types below), n
o need to send an actual email just write in log, update should contain all the tasks of give task_type in which was created last week. It should not send duplicates. Similarly if update_type = daily it should send all the tasks of a given type which were created on that particular day.  We can have multiple trackers, for every tracker there should be unique email

You can create more models if required to same extra info in database
Update_type:
Weekly -> every monday
Daily -> every day at 5 pm
Monthly -> first day of month

```

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
