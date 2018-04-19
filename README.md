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
    * [Setting up Python environment](#installing-python-environment)
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
* Python 3.6.5+

## Installing
### Setting up the Raspberry Pi
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

### Installing Python Environment
1. Installing Python 3.6.5
    ```bash
    $ wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
    $ tar xzvf Python-3.6.0.tgz
    $ cd Python-3.6.0/
    $ ./configure
    $ make
    $ sudo make install
    ```
    
1. Set up virtual environment
    ```bash
    $ apt install virtualenv
    $ virtualenv --python /usr/bin/python3.6 RPI-Temp-sensor # To create virtualenv with python3.6
    $ cd RPI-Temp-sensor
    $ source ./bin/activate # To start working on virtualenv
    $ git clone https://github.com/wnndgws/DS18B20_email_alert.git
    $ cd DS18B20_email_alert
    ```
1. Install requirements
    ```bash
    $ pip install -r requirements.txt
    ```
1. Run using command-line arguments

## Contributing

Please read [CONTRIBUTING.md](https://github.com/WnndGws/DS18B20_email_alert/blob/master/CONTRIBUTING.md) for details on contributing.

## Authors

* [WnndGws](https://github.com/wnndgws)

## Contributors

* [AmmGws](https://github.com/ammgws)
    - Most docstrings in read_temperature.py
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
