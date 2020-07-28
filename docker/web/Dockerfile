FROM python:3.7
MAINTAINER maksim.zaiakin@urfu.me

ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]