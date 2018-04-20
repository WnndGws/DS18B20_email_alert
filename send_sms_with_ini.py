#!/usr/bin/python3
## Send SMS with twilio

import configparser
from twilio.rest import Client
import log_temperature

def send_sms():

    temp = log_temperature.read_temp()
    sms_body = ("Your freezer has been logged at %s degC. Please see your email for more information" % temp)

    config = configparser.ConfigParser()
    config.read('sms-settings.ini')
    account_sid = config['DEFAULT']['account_sid']
    auth_token = config['DEFAULT']['auth_token']
    receiver_ph_number = config['DEFAULT']['receiver_ph_number']
    sender_ph_number = config['DEFAULT']['sender_ph_number']

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to = receiver_ph_number,
        from_ = sender_ph_number,
        body = sms_body
        )

if __name__ == '__main__':
    send_sms()
