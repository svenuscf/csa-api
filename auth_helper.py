import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

load_dotenv()

TOKEN_URL = 'https://api.sse.cisco.com/auth/v2/token'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_secure_access_token():
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=TOKEN_URL, auth=auth)
    return token['access_token']

