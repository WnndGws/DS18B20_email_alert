# DS18B20 Email Alert

This is a python script that can be run on a Raspberry Pi connected to a DS18B20 temperature sensor.
The script will run continuously, and when a temperature threshold is reached, will email a user.

## Getting Started

A Rpi set up, with a DS18B20 connected to the GPIO (see (References)[##References])

### Prerequisites

All code is run on the following system:
* A Raspberry Pi Zero W
* Rasbian Stretch Lite
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

## Deployment

Add additional notes about how to deploy this on a live system
<++>

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* WnndGws

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Original code forked from Pimylifeup
[Pimylifeup](https://github.com/pimylifeup/temperature_sensor)

* Inspiration for project from [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview)

## References
![Image from Adafruit](https://cdn-learn.adafruit.com/assets/assets/000/003/782/medium800/learn_raspberry_pi_breadboard-probe.png?1396801706)
