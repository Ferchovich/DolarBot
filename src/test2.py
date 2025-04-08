import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '1104125067320885398'
CLIENT_SECRET = '6UeJLIU5sxruP0mk_XD7DWfDHy2CEINF'

def get_token():
  data = {
    'grant_type': 'client_credentials',
    'scope': 'identify connections'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post(f'{API_ENDPOINT}/oauth2/token', data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()

token = get_token()
print(token)