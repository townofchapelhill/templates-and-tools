### functions for accessing Sierra resources

import secrets
import requests
import json

def get_token():

    # url = "https://sandbox.iii.com/iii/sierra-api/v5/token"
    url = "https://catalog.chapelhillpubliclibrary.org/iii/sierra-api/v3/token"
    header = {"Authorization": "Basic " + str(secrets.sierra_api_2), "Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, headers=header)
    json_response = json.loads(response.text)
    token = json_response["access_token"]
    return token