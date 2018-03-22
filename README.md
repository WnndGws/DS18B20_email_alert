# DS18B20 Email Alert

This is a python script that can be run on a Raspberry Pi connected to a DS18B20 temperature sensor.
The script will run continuously, and when a temperature threshold is reached, will email a user.

## Getting Started

A Rpi set up, with a DS18B20 connected to the GPIO (see [References](#references))

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


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Original code forked from Pimylifeup
[Pimylifeup](https://github.com/pimylifeup/temperature_sensor)

* Inspiration for project from [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview)

## References
![Image from Adafruit](https://cdn-learn.adafruit.com/assets/assets/000/003/782/medium800/learn_raspberry_pi_breadboard-probe.png?1396801706)
