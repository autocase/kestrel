import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.environment import env_sendgrid_key

logger = logging.getLogger(__name__)


def send_email_to(recipient):
    message = Mail(
        from_email="test@kestralapi.com",
        to_emails=recipient,
        subject="Testing Kestral Email",
        html_content="A sample message",
    )

    message.dynamic_template_data = {"user_name": "A NEW NAME"}
    message.template_id = "d-3365a1e105b746cfaf6e95c8ce944b64"

    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    if env_sendgrid_key:
        sg = SendGridAPIClient(env_sendgrid_key)
        response = sg.send(message)
        return response
    else:
        return False
