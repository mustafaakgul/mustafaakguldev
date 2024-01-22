## mustafaakguldev is a Personal Portfolip Website Repo.

### How to run
* cp .env.base .env
* python3.12 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py collectstatic
* python manage.py runserver