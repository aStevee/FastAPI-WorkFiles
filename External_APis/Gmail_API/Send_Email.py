from API_Conection import service, results
import os



# List the first 10 messages
results = service.users().messages().list(userId='me', maxResults=10).execute()
messages = results.get('messages', [])

for message in messages:
    print(message['id'])


