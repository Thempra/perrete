from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import settings
import traceback

def send_mail(subject,message):
    # create message object instance
    msg = MIMEMultipart()
    
    # setup the parameters of the message
    msg['From'] = settings.SMTP_MAIL
    msg['To'] = settings.MAIL_TO
    msg['Subject'] = subject
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    try:
        #create server
        #server = smtplib.SMTP_SSL(settings.SMTP_ADDRESS, settings.SMTP_PORT)
        server = smtplib.SMTP(settings.SMTP_ADDRESS, settings.SMTP_PORT)
        server.ehlo()
        server.starttls()
        # Login Credentials for sending the mail
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        
    except Exception:
        traceback.print_exc()

