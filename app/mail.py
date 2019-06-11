# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.environment import env_sendgrid_key

logger = logging.getLogger(__name__)


def send_email_to(recipient):
    message = Mail(
        from_email='from_email@example.com',
        to_emails='to@example.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    message.dynamic_template_data = {"user_name": "A NEW NAME"}
    message.template_id = "d-3365a1e105b746cfaf6e95c8ce944b64"

    try:
        sg = SendGridAPIClient(env_sendgrid_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        logger.error(
            "A sendgrid error occurred: {} - {}".format(e.__class__, e.__str__())
        )
        raise e
