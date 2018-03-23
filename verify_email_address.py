#!/usr/bin/python3
## Modified from https://github.com/scottbrady91/Python-Email-Verification-Script

import re
import smtplib
import sys
import dns.resolver

def check_email_regex(input_address):
    """Checks that email matches the format of an email address
    """

    # Simple Regex for syntax checking
    email_regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    # Email address to verify
    address_to_verify = str(input_address)
    # Syntax check
    match = re.match(email_regex, address_to_verify)
    if match == None:
        email_regex_valid = False
    else:
        email_regex_valid = True

    return email_regex_valid

def verify_email_exists(input_address, from_address):
    """
    Checks that an email address exists
    The from_address is the field that the script uses for the SMTP MAIL FROM command
    The to_address is the email to verify
    """

    # Email address to verify
    address_to_test = str(to_address)

    # Get domain for DNS lookup
    splitAddress = address_to_test.split('@')
    domain = str(splitAddress[1])
    print('Domain:', domain)

    # MX record lookup
    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
    server.mail(from_address)
    code, message = server.rcpt(str(address_to_verify))
    server.quit()

    # Assume SMTP response 250 is success
    if code == 250:
        email_exists = True
    else:
        email_exists = False

    return email_exists

if __name__ == '__main__':
    pass
