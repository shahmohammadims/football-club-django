FROM python:alpine
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin
RUN mkdir /football_club
WORKDIR /football_club
ADD . /football_club
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

CMD python manage.py collectstatic --no-input; \
    python manage.py migrate --no-input; \
    python manage.py createsuperuser --phone_number 09130000000 --first_name admin --last_name admin --no-input; \
    gunicorn --bind :8000 football_club.wsgi:application