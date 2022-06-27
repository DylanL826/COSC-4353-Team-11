# COSC-4353-Team-11
Webapp project for Raj Singh's Software Design summer class.

Steps to clone and run locally:

CLONE AND CHECKOUT MAIN BRANCH

git clone -b main https://github.com/DylanL826/COSC-4353-Team-11.git

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
