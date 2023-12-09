run-server:
        python manage.py runserver

migrate:
        python manage.py makemigrations
        python manage.py migrate

create-user:
        python manage.py createsuperuser