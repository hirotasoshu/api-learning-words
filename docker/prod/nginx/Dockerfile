FROM nginx:latest

RUN rm -f /etc/nginx/conf.d/default.conf

COPY ./docker/prod/nginx/django_learning_words.conf /etc/nginx/conf.d/