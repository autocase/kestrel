FROM alpine:latest

# Install necessary allpine packages
RUN apk add --no-cache --update \
        py-pip \
        python3-dev \
        build-base \
        linux-headers \
        pcre-dev \
        postgresql \
        postgresql-dev

COPY . /var/www
WORKDIR /var/www

# Upgrade pip so we don't see that warning
# Install python packages
RUN pip3 install --upgrade pip && pip3 install -r requirements/requirements.txt

# Add gunicorn user
RUN addgroup -g 50 -S www-data;\
    adduser -S -G www-data -u 50 -s /bin/bash -h www-data www-data
USER www-data

# Run the server!
CMD /bin/sh -c 'uwsgi --ini ./app/uwsgi.ini --py-autoreload 1'

