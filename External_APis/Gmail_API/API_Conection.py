import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from pathlib import Path
import os

"""
FURUTE DOCUMENTATION HERE

"""

# OAuth 2.0 setup

potential_path_1 = Path(os.getcwd()) / "credentials/client_secret_1048033872747-o60hh2aq6lmgejb0d8qas0o60vqueufm.apps.googleusercontent.com.json"
potential_path_2 = Path(os.getcwd()) / "External_APis/Gmail_API/credentials/client_secret_1048033872747-o60hh2aq6lmgejb0d8qas0o60vqueufm.apps.googleusercontent.com.json"

if potential_path_1.exists():
    CLIENT_SECRET_FILE = potential_path_1
elif potential_path_2.exists():
    CLIENT_SECRET_FILE = potential_path_2
else:
    raise FileNotFoundError(f"Client secret file not found in either path!\nThis is the current path -> {os.getcwd()}")

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


credentials = None

# Check if token.pickle file exists
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

# If there are no valid credentials, authenticate
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

# Build the Gmail API client
service = build(API_NAME, API_VERSION, credentials=credentials)



if __name__ == "__main__":

    # List the first 10 messages
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])

    for message in messages:
        print(message['id'])
