# Django Tasklist App
## Simple tasklist app, made to a small, few employee locksmith company, to help them handle their daily/weekly tasks.

Easily customisable and adjustable.

Made with [Django Python Framework](https://www.djangoproject.com/)

In the course: https://terokarvinen.com/2021/python-web-service-from-idea-to-production-2022/

**App running:** http://anttihalonen.rocks/

**Current Version: Beta**
- Fully functional, but plenty of features and polishing can be done with flexible timeframe, and minimal programming skills.

*01.06.2022 - This app was developed in around 24h, with about 7days knowledge of Django and Python*

Download source: [Tasklist App](https://github.com/therealhalonen/django_tasklist/archive/refs/heads/main.zip)

## Installation instructions:

```bash

$ git clone https://github.com/therealhalonen/django_tasklist
$ cd django_tasklist
$ sudo apt-get -y install virtualenv
$ virtualenv --system-site-packages -p python3 env/
$ source env/bin/activate
$ pip install -r requirements.txt
```
Now you have to create a Django Secret Key in your preferred terminal!
```console
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Copy the output, and add it to the `settings.py`

```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR KEY HERE'
```
Browse back to the project folder that has manage.py
```console
$ ./manage.py migrate
$ ./manage.py createsuperuser
# give your details
$ ./manage.py runserver
```
Go to http://127.0.0.1:8000/ with your browser. Firefox preferred.

Profit!

## Optional feature:
*If you want to have new users to be registered as inactives, and activate them through admin panel,
do the following AFTER YOU HAVE AN ADMIN USER READY*

```console
micro job/models.py
```
Uncomment all:
```python
#@receiver(pre_save, sender=User)
#def set_new_user_inactive(sender, instance, **kwargs):
#    if instance._state.adding is True:
#        print("Creating Inactive User")
#        instance.is_active = False
#    else:
#        print("Updating User Record")
```

## Screenshots:

Front:

![Image](https://github.com/therealhalonen/python_web_service/blob/master/pw6/res/list_view.png)

Delete:

![Image](https://github.com/therealhalonen/python_web_service/blob/master/pw6/res/delete_view.png)

Detailed:

![Image](https://github.com/therealhalonen/python_web_service/blob/master/pw6/res/detail_view.png)

Create:

![Image](https://github.com/therealhalonen/python_web_service/blob/master/pw6/res/create_view.png)


