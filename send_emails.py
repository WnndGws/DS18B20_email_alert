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
def send_email(sender_email, password, receiver_name, receiver_email, template_file):
    """Takes click options, and sends an email
    """

    print(f'{sender_email}: {receiver_name}, {receiver_email}')
    #with open(template_file, 'r', encoding='UTF-8') as tf:
        #template_file_content = tf.read()
    #return Template(template_file_content)

    #names, emails = get_contacts('mycontacts.txt') # read contacts
    #message_template = read_template('message.txt')
#
    ## set up the SMTP server
    #s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
    #s.starttls()
    #s.login(MY_ADDRESS, PASSWORD)
#
    ## For each contact, send the email:
    #for name, email in zip(names, emails):
        #msg = MIMEMultipart()       # create a message
#
        ## add in the actual person name to the message template
        #message = message_template.substitute(PERSON_NAME=name.title())
#
        ## Prints out the message body for our sake
        #print(message)
#
        ## setup the parameters of the message
        #msg['From']=MY_ADDRESS
        #msg['To']=email
        #msg['Subject']="This is TEST"
#
        ## add in the message body
        #msg.attach(MIMEText(message, 'plain'))
#
        ## send the message via the server set up earlier.
        #s.send_message(msg)
        #del msg
#
    ## Terminate the SMTP session and close the connection
    #s.quit()

if __name__ == '__main__':
    send_email()
