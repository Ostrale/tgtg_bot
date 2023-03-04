from tgtg import TgtgClient
# need to create a data.py file with the following variables : myaccess_token, myrefresh_token, myuser_id, mycookie, myemail_send, mypassword, myemail_recipient
from data import myaccess_token, myrefresh_token, myuser_id, mycookie, myemail_send, mypassword, myemail_recipient 
import time
import smtplib
from email.mime.text import MIMEText

def get_info():
    """_summary_ : get the credentials for the tgtg api for the first time
    see : https://github.com/ahivert/tgtg-python
    """
    client = TgtgClient(email="<your_email_use_for_togoodtogo>")
    credentials = client.get_credentials()
    print(credentials)

def send_email (sender_email, sender_password, recipient_email, message_subject, message_body):
    """_summary_ : send an email with the given parameters using the gmail smtp server 

    :param string sender_email: the email address of the sender
    :param string sender_password: the password of the sender email address
    :param string recipient_email: the email address of the recipient (can be the same as the sender)
    :param string message_subject: the subject of the email
    :param string message_body: the body of the email
    """
    # Paramètres SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Contenu du message
    message = MIMEText(message_body)
    message['Subject'] = message_subject
    message['From'] = sender_email
    message['To'] = recipient_email

    # Connexion au serveur SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Envoi du message
        server.sendmail(sender_email, recipient_email, message.as_string())

    print('Le message a été envoyé avec succès.')


def find(theaccess_token, therefresh_token, theuser_id, thecookie):
    """_summary_ : find the items that are available at the stores that are in the favorites list of the user and send an email if there is at least one item available

    :param string theaccess_token: your access token
    :param string therefresh_token: your refresh token
    :param string theuser_id: your user id
    :param string thecookie: your cookie
    """
    client = TgtgClient(access_token=theaccess_token, refresh_token=therefresh_token, user_id=theuser_id, cookie=thecookie)

    favorites = client.get_items()
    for favorite in favorites:
        item = favorite['item']
        store = favorite['store']
        display_name = favorite['display_name']
        items_available = favorite['items_available']
        favorite = favorite['favorite']
        if items_available > 0:
            txt = f"item(s) is available at {display_name} and has {items_available} items available"
            print(txt)
        else:
            txt = f"item(s) is not available at {display_name}"
            print(txt)
            # return
    
        sub = f"item(s) is available at {display_name}"
        send_email(myemail_send, mypassword, myemail_recipient, sub, txt)

if __name__ == "__main__":
    find(myaccess_token, myrefresh_token, myuser_id, mycookie)

