from flask import request

from gmail_send import send_email


def send_feedback():
    json_data = request.get_json()

    if json_data:
        name = json_data.get('name')
        email = json_data.get('email')
        phone = json_data.get('phoneNumber')
        introduction = json_data.get('introduction')
        text = json_data.get('text')

        message = f'{name}\n{email}\n{phone}\n{introduction}\n{text}'

            # send message to email
        if message.strip() != '':
            send_email(message=message)
        else:
            print('Form is Empty!')


