# Meeting 2 - 9/24/18

## Raspberry Pi
GPIO Pins allow the raspberry pi to output voltage and read inputs from electronic devices.
![GPIO Pins](images/gpio-pins-pi2.jpg "GPIO Pins")
![GPIO Pin Diagram](images/gpio-numbers-pi2.png "GPIO Pin Diagram")
### Example code using gpiozero library
```python3
from gpiozero import LED
from time import sleep

led = LED(14)

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
```
## Other useful resources
* [Learn X in Y minutes](https://learnxinyminutes.com/)
* [Raspberry Pi docs](https://www.raspberrypi.org/documentation/)
* [gpiozero docs](https://gpiozero.readthedocs.io/en/stable/)
* [Python3 docs](https://docs.python.org/3/)
