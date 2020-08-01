FROM python:3.7
MAINTAINER maksim.zaiakin@urfu.me

ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements/dev.txt

COPY ./docker/dev/web/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]