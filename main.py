#!/usr/bin/python3
## Brings everything together

import read_temperature
import verify_email_address

import configparser
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
    print(message) # Prints out the message body for our sake

    ## setup the parameters of the message
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']="This is TEST"

    ## Add in the message body
    msg.attach(MIMEText(message, 'plain'))

    ## Send the message via the server set up earlier.
    #s.send_message(msg)
    del msg #cleanup
#
    ## Terminate the SMTP session and close the connection
    s.quit()

def latest_2_temps():
    '''Keeps the last 2 temperatures, to prevent false positive emails. Will only send email when both are above a threshold
    '''

    latest_2_temps = []
    if len(latest_2_temps) == 2:
        latest_2_temps.pop(0)
        latest_2_temps.append(read_temperature.read_temp())
    else:
        latest_2_temps.append(read_temperature.read_temp())

    return(latest_2_temps)

if __name__ == '__main__':
    print(latest_2_temps())
