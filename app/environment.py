import os

from dotenv import load_dotenv
from falcon import HTTPInternalServerError

load_dotenv()
# Build an object to manage our db connections.
try:
    env_db_host = os.environ["DB_HOST"]
    env_db_name = os.environ["DB_NAME"]
    env_db_user = os.environ["DB_USER"]
    env_db_pass = os.environ["DB_PASS"]

    connection = "postgresql+psycopg2://{user}:{pwd}@{host}/{name}".format(
        user=env_db_user, pwd=env_db_pass, host=env_db_host, name=env_db_name
    )
except KeyError:
    raise HTTPInternalServerError(
        description="The server could not reach the database, "
        "please contact your account manager.",
        code=9,
    )
