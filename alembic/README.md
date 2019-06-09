# Alembic Instructions
Create a new migration: `$ alembic revision -m "[revision description]"`

Run migrations to latest: `$ alembic upgrade head`

Downgrade back to the beginning: `$ alembic downgrade base`

Downgrade back 1: `$ alembic downgrade -1`
