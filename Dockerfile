FROM python:alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin
ADD . .
RUN pip install --upgrade pip
RUN pup install -r requirments.txt
CMD python manage.py makemigrations account --no-input && \
    python manage.py makemigrations exercise --no-input && \
    python manage.py makemigrations payment --no-input && \
    python manage migrate --no-input && \
    python manage.py --phone_number=09130000000 --firstname=admin --lastname=admin; \
    python manage.py runserver 127.0.0.1:8000