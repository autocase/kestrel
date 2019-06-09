[![CircleCI](https://circleci.com/gh/autocase/kestrel.svg?style=svg)](https://circleci.com/gh/autocase/kestrel)
[![codecov](https://codecov.io/gh/autocase/kestrel/branch/master/graph/badge.svg)](https://codecov.io/gh/autocase/kestrel)
[![Requirements Status](https://requires.io/github/autocase/kestrel/requirements.svg?branch=development)](https://requires.io/github/autocase/kestrel/requirements/?branch=development)
[![Updates](https://pyup.io/repos/github/autocase/kestrel/shield.svg)](https://pyup.io/repos/github/autocase/kestrel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Kestrel
A heavily opinionated [Falcon](https://github.com/falconry/falcon) boilerplate. 

## What's Included
- [Postgres](https://www.postgresql.org/) with SQLAlchemy and Psycopg2
- [UWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) used to run Falcon
- [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/) for request and schema serialization
- [Nginx](https://www.nginx.com/) to serve Falcon
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations
- [CircleCI](https://circleci.com/) to run tests 

### For Development
- [OpenAPI](https://swagger.io/specification/)/Swagger Viewer for API testing
- [Flake8](http://flake8.pycqa.org/en/latest/) for linting
- [Sphinx](http://www.sphinx-doc.org) to generate html documentation


# Requirements
[Docker](https://docs.docker.com/install/)

# Installation
1. Clone this repo
2. Open up your terminal/powershell and navigate to the project folder.
3. Run Docker Compose to start the VM
`docker-compose up -d`
4. Go to `http://localhost`!

## Developing locally
While Docker is running, you can install all the dependencies with `pipenv install --dev` and
any changes you make should automatically be reflected on `localhost`.

### Testing
Some sample tests have been written in PyTest, running them is as simple as typing `pytest` in the
directory. This will go through the repository and search for any files starting with `test`, which 
are located in the tests folders.

# Structure
## Alembic
[Alembic](https://alembic.sqlalchemy.org/en/latest/) is a lightweight database migration tool for 
usage with the SQLAlchemy Database Toolkit for Python.
## App
The main Falcon application
### App.py
The start of the API service
### Middleware
Functions that are called before and after each of the resources.
### Resources
All of your endpoints and how you deal with API requests go here
