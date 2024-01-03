# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def send_sms():
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    account_sid = 'AC56b6ab8668d3b57e5f19899bf92b793a'
    auth_token = '8d83627465d397218aec6890e8432d3c'

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Warning Alert !!",
            from_='+19253504959',
            to='+918248236368'
        )
