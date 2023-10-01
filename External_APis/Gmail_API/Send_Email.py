from . import API_Conection
import os
import base64
from email.mime.text import MIMEText


"""
SEND EMAIL (post <useremail>)


"""

class PauEmail:
    def create_message(to, subject, message_text):
        """Create a MIMEText message to be sent via Gmail API."""
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = "paumat17@gmail.com"
        message['subject'] = subject
        # Base64 encode the MIME message.
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')}

    def send_message(service, user_id, message):
        """Use the Gmail API's send method to send the email."""
        try:
            message = service.users().messages().send(userId=user_id, body=message).execute()
            print(f"Message sent: {message['id']}")
            return f"Message sent: {message['id']}"
        except Exception as e:
            print(f"An error occurred: {e}")
            return None






if __name__ == "__main__":
    # Example usage
    recipient = "carolinaforner@gmail.com"
    subject = "PRUEBA PRUEBA PRUEBA PRUEBA PRUEBA PRUEBA PRUEBA PRUEBA"
    message_text = "Hola Hola Hola  esto es una prueba, esto es un mensaje enviado desde un servidor lololol,\n si ves es esto es que  como coño para desayunar"

    # Example of how to send a message:
    mime_message = PauEmail.create_message( recipient, subject, message_text)
    PauEmail.send_message(API_Conection.service, 'me', mime_message)