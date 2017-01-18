#!/usr/bin/env python
"""Code to control the CCNA Lab
"""

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

__author__ = "Benjamin Koderisch"
__maintainer__ = __author__
__email__ = "b.koderisch@gmail.com"


pin = port.PA12

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        in = raw_input("1: start Programm    2: reboot   3: shutdown")
        if(in == 1):
            gpio.output(pin, 1)
        if(in == 2):
            if(gpio.input(pin)):
                gpio.output(pin, 0)
                for i in range 5:
                    print"wait..."
                    sleep(2)
                gpio.output(pin, 1)
                print"done!"
        if(in == 3):
            gpio.output(pin, 0)

except KeyboardInterrupt:
    gpio.output(pin, 0)
    print ("Goodbye!")
