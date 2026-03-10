FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install django djangorestframework requests

CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"