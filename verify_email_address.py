#!/usr/bin/python3
## Modified from https://github.com/scottbrady91/Python-Email-Verification-Script

import re
import smtplib
import sys
import dns.resolver

def verify_email(input_address, from_address):
    """
    Checks that an email address is both valid, and exist
    The from_address is the field that the script uses for the SMTP MAIL FROM command
    The input_address is the email to verify
    """

    # Simple Regex for syntax checking
    email_regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

    # Email address to verify
    address_to_verify = str(input_address)

    # Syntax check
    match = re.match(email_regex, address_to_verify)
    if match == None:
        print('Bad')
    else:
        # Get domain for DNS lookup
        splitAddress = address_to_verify.split('@')
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

        #print(code)
        #print(message)

        # Assume SMTP response 250 is success
        if code == 250:
            print('Success')
        else:
            print('Bad')

if __name__ == '__main__':
    verify_email("test@gmail.com", "test2@gmail.com")
