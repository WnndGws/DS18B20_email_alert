#!/usr/bin/python3

import click
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template

@click.command()
@click.option('--sender-email', prompt="Sender email used to log into the SMTP server", type=str, help="Sender's email address")
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help="Password to log into email server")
@click.option('--receiver-name', prompt="Name of receiver", type=str, help="Name of the email recipient")
@click.option('--receiver-email', prompt="Email address to send email to", type=str, help="Email address of the recipient")
@click.option('--template-file', type=click.Path(), default="./email-template.txt.example", help="The file the email template should be read from. DEFAULT=./email-template.txt")
@click.option('--smtp-host', type=str, default="smtp.gmail.com", help="The URL for the smtp server to send emails with. DEFAULT=smtp.google.com")
@click.option('--smtp-port', type=int, default=587, help="The port to use with the SMTP host. DEFAULT=587")
def send_email(sender_email, password, receiver_name, receiver_email, template_file, smtp_host, smtp_port):
    """Takes click options, and sends an email
    """

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

if __name__ == '__main__':
    send_email()
