FROM python:3.8-slim-buster
WORKDIR /var/www
ENV PIP_NO_CACHE_DIR=false
COPY Pipfile Pipfile.lock /var/www/

RUN set -ex \
        && apt-get update \
        && apt-get install -y --no-install-recommends \
        gcc g++ libpq-dev \
        && pip install --upgrade pip pipenv \
        && pipenv install --system --deploy \
        && apt-get purge -y --auto-remove \
        gcc g++ \
        && rm -rf /var/lib/apt/lists/*

USER www-data
COPY . /var/www/

CMD /bin/sh -c 'alembic upgrade heads && uwsgi --ini app/uwsgi.ini'
