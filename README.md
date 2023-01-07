* pip3 install 'django<4' (to install django long term support)
* django-admin startproject django_todo . (to start a new project named 'django_todo'. the dot is used to start the project in the current directory)
* python3 manage.py runserver (to start the server)
* python3 manage.py startapp todo (to create a new app named 'todo')

* python3 manage.py makemigrations (to apply all migrations)
* python3 manage.py showmigrations (to show what wil be updated)
* python3 manage.py migrate (to update database )
* python3 manage.py createsuperuser (to create a admin user)

* coverage run --source=todo manage.py test (to create a test report after instaling coverage('pip3 install coverage'))