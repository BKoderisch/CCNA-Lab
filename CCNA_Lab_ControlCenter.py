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


sw1 = port.PA12
sw2 = port.PA11
r1 = port.PA6


gpio.init()
gpio.setcfg(sw1, gpio.OUTPUT)
gpio.setcfg(sw2, gpio.OUTPUT)
gpio.setcfg(r1, gpio.OUTPUT)

try:
    gpio.output(port.PA12, 1) 
    gpio.output(port.PA11, 1)
    gpio.output(port.PA6, 1)
    
    print ("Press CTRL+C to exit")
    while True:
        pin = input("sw1    sw2     r1 \n")
        affenkind = input("1: start Programm    2: reboot   3: shutdown\n")
        if(affenkind == 1):
            gpio.output(pin, 0)
        if(affenkind == 2):
            if(gpio.input(pin)):
                gpio.output(pin, 1)
                for i in range (5):
                    print"wait..."
                    sleep(2)
                gpio.output(pin, 0)
                print"done!"
        if(affenkind == 3):
            gpio.output(pin, 1)

except KeyboardInterrupt:
    gpio.output(port.PA12, 1) 
    gpio.output(port.PA11, 1)
    gpio.output(port.PA6, 1)
    print ("Goodbye!")
