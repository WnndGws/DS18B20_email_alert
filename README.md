# DS18B20 Email Alert

This is a python script that can be run on a Raspberry Pi connected to a DS18B20 temperature sensor.
The script will run continuously, and when a temperature threshold is reached, will email a user.

## Getting Started

* A Rpi set up, with a DS18B20 connected to the GPIO (see [References](#references))
* An email account to send emails from (A free gmail account will suffice)
* An account with [Twilio](https://www.twilio.com/sms/pricing/)(OPTIONAL)
    - Only if you would like to send an SMS when an alert is triggered

### Prerequisites

All code is run on the following system:
* A Raspberry Pi Zero W
    - Any Rpi should be able to work, as long as it can handle Rasbian and Python 3
* Rasbian Stretch Lite
    - Again, any distro that runs on the Rpi should work, this is just what I am using
* Python 3

### Installing

0. Run raspi-config
    ```bash
    sudo raspi-config
    reboot
    ```
1. Update the Rpi
    ```bash
    sudo rpi-update
    reboot
    ```
2. Update Rasbian
    ```bash
    sudo apt update
    sudo apt upgrade
    reboot
    ```

## Running the tests

Explain how to run the automated tests for this system
<++>

### Break down into end to end tests

Explain what these tests test and why
<++>

```
Give an example
<++>
```

### And coding style tests

Explain what these tests test and why
<++>

```
Give an example
<++>
```

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

* Inspiration for project from [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview)

## References
* This project uses [Twilio](https://www.twilio.com/sms/pricing/) to send it's SMS messages

* ![Image from Adafruit](https://cdn-learn.adafruit.com/assets/assets/000/003/782/medium800/learn_raspberry_pi_breadboard-probe.png?1396801706)
