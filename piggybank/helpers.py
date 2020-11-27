import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# get access token
def get_headers(refresh_token):
  # To refresh an access token, POST the following parameters as application/x-www-form-urlencoded to
  endpoint = 'https://api-sandbox.starlingbank.com/oauth/access-token'

  # client id & secret for this CS50Web App
  client_id = os.getenv('CLIENT_ID')
  client_secret = os.getenv('CLIENT_SECRET')
  payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret, 'grant_type': "refresh_token"}

  res = requests.post(endpoint, data = payload)
  if res.status_code != 200:
    raise Exception("ERROR: API request unsuccessful.")

  # json() is already a Python dictionary
  oauth = res.json()
  headers = {"Authorization": "Bearer " + oauth['access_token']}

  return headers
