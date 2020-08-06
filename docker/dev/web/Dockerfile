FROM python:3.7
MAINTAINER maksim.zaiakin@urfu.me

ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements/dev.txt

COPY ./docker/dev/web/entrypoint.sh /entrypoint.sh
COPY ./docker/dev/web/createsuperuser.sh /createsuperuser.sh
COPY ./docker/dev/web/migrate.sh /migrate.sh

RUN chmod +x /entrypoint.sh
RUN chmod +x /createsuperuser.sh
RUN chmod +x /migrate.sh

ENTRYPOINT ["/entrypoint.sh"]