import os
import jwt


VALID_USERNAME = os.getenv('VALID_USERNAME')
VALID_PASSWORD = os.getenv('VALID_PASSWORD')
ADMIN_TOKEN = os.getenv('ADMIN_TOKEN')
DEFAULT_USER_TOKEN = os.getenv('DEFAULT_USER_TOKEN')


def is_admin(username, password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        token_payload = {
            'username': username,
        }
        token = jwt.encode(token_payload, str(ADMIN_TOKEN), algorithm='HS256')

        return token
    else:
        default_token = str(DEFAULT_USER_TOKEN)
        return default_token
