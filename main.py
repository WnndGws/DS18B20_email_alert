#!/usr/bin/python3
## Brings everything together

import log_temperature
import verify_email_address

import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template
import sys
import time

def send_emails():
    config = configparser.ConfigParser()
    config.read('email-settings.ini')
    sender_email = config['DEFAULT']['sender_email']
    sender_password = config['DEFAULT']['sender_password']
    smtp_host = config['DEFAULT']['sender_smtp_host']
    smtp_port = config['DEFAULT']['sender_smtp_port']
    receiver_name = config['DEFAULT']['receiver_name']
    receiver_email = config['DEFAULT']['receiver_email']
    template_file = 'email-template.ini'

    test_email_regex = verify_email_address.verify_email_regex(receiver_email)

    if test_email_regex:
        email_exists = verify_email_address.verify_email_exists(receiver_email, sender_email)

    if not email_exists:
        print("The receiver-email could not be verified. Please run the program again with a different receiver-email")
        exit()

    with open(template_file, 'r', encoding='UTF-8') as tf:
        template_file_content = tf.read() #Reads file, and uses that as template

    ## set up the SMTP server
    s = smtplib.SMTP(host=smtp_host, port=smtp_port)
    s.starttls()
    s.login(sender_email, password)

    ## Send the email:
    msg = MIMEMultipart()       # create a message
    message = template_file_content.replace("{NAME}", receiver_name.title()) # Add in the actual person name to the message template
    #print(message) # Prints out the message body for our sake
    part = MIMEBase('application', "octet-stream") # create an attachment file
    part.set_payload(open("./logs/freezer01_temperature.log","rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))

    ## setup the parameters of the message
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']="This is TEST"

    ## Add in the message body
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(part) # Attach log file

    ## Send the message via the server set up earlier.
    s.send_message(msg)
    del msg #cleanup

    ## Terminate the SMTP session and close the connection
    s.quit()

def keep_latest_2_temps():
    '''Keeps the last 2 temperatures, to prevent false positive emails. Will only send email when both are above a threshold
    '''
    if len(latest_2_temps) == 2:
        latest_2_temps.pop(0)
        latest_2_temps.append(log_temperature.read_temp())
    else:
        latest_2_temps.append(log_temperature.read_temp())

    return(latest_2_temps)

if __name__ == '__main__':
    latest_2_temps = [-100, -100]
    while True:
        log_temperature.log_temps()
        keep_latest_2_temps()
        if (latest_2_temps[0] and latest_2_temps[1]) > 20:
            send_emails()
            time.sleep(43200) # sleep 12 hours to prevent a million emails being sent
        time.sleep(900)
