import os

from dotenv import load_dotenv
from falcon import HTTPInternalServerError

load_dotenv()


def create_connection():
    # Build an object to manage our db connections.
    try:
        db_host = os.environ["DB_HOST"]
        db_name = os.environ["DB_NAME"]
        db_user = os.environ["DB_USER"]
        db_pass = os.environ["DB_PASS"]

        return "postgresql+psycopg2://{user}:{pwd}@{host}/{name}".format(
            user=db_user, pwd=db_pass, host=db_host, name=db_name
        )
    except KeyError:
        raise HTTPInternalServerError(
            description="The server could not reach the database, "
            "please contact your account manager.",
            code=9,
        )


IN_PRODUCTION = os.getenv("IN_PRODUCTION", False)
