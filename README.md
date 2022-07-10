# COSC-4353-Team-11
Web app project for Raj Singh's Software Design summer class.

Steps to clone and run locally:

CLONE AND CHECKOUT

git clone *url*

CREATE VIRTUAL ENVIRONEMENT

python3 -m venv venv

ACTIVATE VENV

source venv/bin/activate

INSTALL DEPENDENCIES

python3 -m pip install -r requirements.txt

CHANGE DIRECTORIES

cd bloggitt

MAKEMIGRATIONS

python3 manage.py makemigrations

MIGRATE

python3 manage.py migrate

CREATE SUPERUSER

python3 manage.py createsuperuser

RUN

python3 manage.py runserver
