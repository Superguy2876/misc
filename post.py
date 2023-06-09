import requests
import json
import base64
from totp import totp
import pprint


def make_request(url, token, data):
    headers = {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

def pre_request(url, token, data):
    headers = {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json'
    }
    req = requests.Request('POST', url, data=json.dumps(data), headers=headers)
    prepped = req.prepare()
    return prepped

if __name__ == "__main__":
    url = input('Enter the URL: ')
    userid = input('Enter your email: ')
    password = input('Enter your password: ')
    
    data = {
        "example_field": "example",
        "contact_email": userid,
    }
    
    secret = userid + password

    byte_secret = bytearray(secret, 'ascii')


    base32_secret = base64.b32encode(byte_secret).decode('ascii')

    otp = totp(base32_secret)

    pre_token = f'{userid}:{otp}'
    token = base64.b64encode(pre_token.encode('ascii')).decode('ascii')

    # prepped = pre_request(url, token, data)
    # print(prepped.headers)
    # pprint.pprint(prepped.body)
    response = make_request(url, token, data)
    print(response.status_code)
    print(response.text)