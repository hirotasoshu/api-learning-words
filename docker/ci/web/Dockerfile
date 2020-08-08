FROM python:3.7
MAINTAINER maksim.zaiakin@urfu.me

ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements/prod.txt
RUN pip install -r requirements/dev.txt

COPY ./docker/prod/web/entrypoint.sh /entrypoint.sh
COPY ./docker/prod/web/collectstatic.sh /collectstatic.sh
COPY ./docker/prod/web/createsuperuser.sh /createsuperuser.sh
COPY ./docker/prod/web/migrate.sh /migrate.sh


RUN chmod +x /entrypoint.sh
RUN chmod +x /collectstatic.sh
RUN chmod +x /createsuperuser.sh
RUN chmod +x /migrate.sh

ENTRYPOINT ["/entrypoint.sh"]