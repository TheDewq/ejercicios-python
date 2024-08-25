# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import time
import test
from _thread import start_new_thread
from machine import Pin
from esp32 import NVS
#nvs configs
nvs = NVS("VARS")
nvs.set_i32("LED_DELAY", 1)
nvs.commit()
#Pin config in this thread
btn = Pin(0, Pin.IN, Pin.PULL_UP)

#thread vars
i = 0;

#bluetooth config
test.bluetooth_connect()

#start pin thread


def change_PWM_delay(pin):
    print("changing delay...")
    delay = nvs.get_i32("LED_DELAY")
    delay = delay + 1
    if delay > 16:
        delay = 1
        
    
    
    print("new delay: "+str(delay))
        
    nvs.set_i32("LED_DELAY", delay)
    nvs.commit()
    
btn.irq(trigger=Pin.IRQ_FALLING, handler=change_nvs_delay)
start_new_thread(test.led_inter, ())


        
