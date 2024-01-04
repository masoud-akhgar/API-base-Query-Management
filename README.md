# API-based Query Management
A Cloud Project using Django, sqlite3 file as the database, MVP model, Postman.

This project is completely based on Django, so it is not provided any UI design.

Django settings for cloud_project project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

to run, clone the project and run in commandLine:
python manage.py runserver
Then, open the link below :
http://127.0.0.1:8000/

go to /sign up, and then /gettoken,
feel free to work with Postman

python manage.py createsuperuser didn't work, It must be changed to python manage.py createsuperuser --database=users_db

# Convert CSV to Sqlite
sqlite3 db.sqlite3
.mode csv
.import vgsales.csv app_vgsales

# Docker, yml and json files are pasted in the main folder to be accesible
