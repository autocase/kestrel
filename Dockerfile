FROM python:3.7.3-alpine3.9

# Install necessary allpine packages
RUN apk add --no-cache --update \
        build-base \
        linux-headers \
        pcre-dev \
        postgresql \
        postgresql-dev

COPY . /var/www
WORKDIR /var/www

# Upgrade pip so we don't see that warning
# Install python packages
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --deploy --ignore-pipfile --system

# Add gunicorn user
RUN addgroup -g 50 -S www-data;\
    adduser -S -G www-data -u 50 -s /bin/bash -h www-data www-data
USER www-data

# Run the server!
CMD /bin/sh -c 'uwsgi --ini ./app/uwsgi.ini --py-autoreload 1'

