FROM python:3.7.3-alpine3.9

WORKDIR /var/www

COPY Pipfile Pipfile.lock /var/www/

RUN set -ex \
        # Build deps
        && apk add --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
        && apk add --repository http://dl-cdn.alpinelinux.org/alpine/v3.6/main --no-cache \
        postgresql=9.6.13-r0 postgresql-dev=9.6.13-r0 \
        # Install python deps
        && pip install --no-cache-dir --upgrade pip pipenv \
        && pipenv install --deploy --system \
        # Cleanup build deps
        && apk del .build-deps postgresql-client postgresql \
        # Add gunicorn user
        && addgroup -g 50 -S www-data \
        && adduser -S -G www-data -u 50 -s /bin/bash -h www-data www-data

USER www-data

COPY . /var/www/

# Run the server!
CMD /bin/sh -c 'uwsgi --ini ./app/uwsgi.ini --py-autoreload 1'

