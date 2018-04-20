#!/usr/bin/python3
## Brings everything together

import log_temperature
import verify_email_address
import send_emails_with_ini

import time

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
            send_emails_with_ini.send_email()
            seconds_slept = 0
            while seconds_slept < 43200: # keep logging but dont email
                time.sleep(900)
                seconds_slept += 900
                log_temperature.log_temps()
        time.sleep(900)
