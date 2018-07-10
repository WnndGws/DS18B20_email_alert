# DS18B20 Email Alert

This is a python script that can be run on a Raspberry Pi connected to a DS18B20 temperature sensor.
The script will run continuously, and when a temperature threshold is reached, will email a user.


## Getting Started

* A Rpi set up, with a DS18B20 connected to the GPIO (see [References](#references))
* An email account to send emails from (A free gmail account will suffice)
* (OPTIONAL) An account with [Twilio](https://www.twilio.com/sms/pricing/) (see [References](#references))
    - Only if you would like to send an SMS when an alert is triggered

## Table of Contents
1. [Prerequisites](#prerequisites)
1. [Installing](#installing)
    * [Setting up the RPI](#setting-up-the-raspberry-pi)
    * [Setting up logging environment](#installing-logging-environment)
    * [Setting up flask ui](#installing-flask-environment)
1. [Contributing](#contributing)
1. [Authors](#authors)
1. [Acknowledgments](#acknowledgments)
1. [References](#references)

## Prerequisites

All code is run on the following system:
* A Raspberry Pi Zero W
    - Any Rpi should be able to work, as long as it can handle Rasbian and Python 3
* Rasbian Stretch Lite
    - Again, any distro that runs on the Rpi should work, this is just what I am using
* Python 3

## Installing
### Setting up the Raspberry Pi
0. Set up the Rpi to run headless
    * Create a file in the boot partition with `touch ssh`
    * Create a FULL wpa_supplicant.conf file in the /etc folder on the SD card
    ```bash
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1
        country=AU

        network={
            ssid="Your network SSID"
            psk="Your WPA/WPA2 security key"
            key_mgmt=WPA-PSK
        }
    ```
0. Run raspi-config
    ```bash
    $ raspi-config
    reboot
    ```
1. Update the Rpi
    ```bash
    $ rpi-update
    reboot
    ```
2. Update Rasbian
    ```bash
    $ apt update
    $ apt upgrade
    reboot
    ```

### Installing logging Environment
1. Set up virtual environment
    ```bash
    $ apt install python3-pip
    $ pip3 install virtualenv
    $ virtualenv --python /usr/bin/python3 RPI-Temp-sensor # To create virtualenv with python3.6
    $ cd RPI-Temp-sensor
    $ source ./bin/activate # To start working on virtualenv
    $ git clone https://github.com/wnndgws/DS18B20_email_alert.git
    $ cd DS18B20_email_alert/logging
    ```
1. Install requirements
    ```bash
    $ pip install -r requirements.txt
    ```
1. Run using command-line arguments
    ```bash
    $ cp ./email-settings.ini.example ./email-settings.ini
    $ cp ./email-template.ini.example ./email-template.ini
    ```
    * Edit the two ini files to match your needs
1. Run the main program
    ```bash
    $ python main.py
    ```

### Installing Flask Environment
1. Set up Flask environment
    ```bash
    $ cd $HOME/RPI-Temp-sensor/DS18B20_email_alert/webapp
    $ source ../bin/activate # To make sure virtualenv is still active
    $ pip install -r requirements.txt
    ```
1. Set up a webserver running with Apache
    ```bash
    $ apt install supervisor
    ```

1. Set up the Flask configuration file
    * Edit supervisor.conf to reflect the paths etc.
        * They should be correct though

1. Symlink the supervisor conf file to the correct location
    ```bash
    $ ln supervisor.conf /etc/supervisor/conf.d/supervisor.conf
    ```
 
1. Run the flask server
    ```bash
    python __init__.py
    ```
1. On another computer go to '<rpi-local-ip>:8000' to test server

## Contributing

Please read [CONTRIBUTING.md](https://github.com/WnndGws/DS18B20_email_alert/blob/master/CONTRIBUTING.md) for details on contributing.

## Authors

* [WnndGws](https://github.com/wnndgws)

## Contributors

* [AmmGws](https://github.com/ammgws)
    - Most docstrings in log_temperature.py
    - Spelling and formatting of other code

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Original temperature code forked from Pimylifeup
[Pimylifeup](https://github.com/pimylifeup/temperature_sensor)

* Original email code forked from arjunkrishnababu96
[arjunkrishnababu96](https://gist.github.com/arjunkrishnababu96/5c96ef3306b92120696a44b92db8947f)

* Original email-address verification code forked from [scottbrady91](https://github.com/scottbrady91/Python-Email-Verification-Script
)

* Inspiration for project from [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview)

## References
* This project uses [Twilio](https://www.twilio.com/sms/pricing/) to send it's SMS messages

* Image from Adafruit
![Image from Adafruit](https://cdn-learn.adafruit.com/assets/assets/000/003/782/medium800/learn_raspberry_pi_breadboard-probe.png?1396801706)
