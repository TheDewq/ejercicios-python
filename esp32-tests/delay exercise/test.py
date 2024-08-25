from bluetooth import BLE
from machine import Pin
from esp32 import NVS
import time
import sys


led = Pin(2, Pin.OUT)


def bluetooth_connect():
    ble = BLE()
    ble.active(True)
    print("bluetooth status")
    print(ble.active())


def led_inter():
    nvs = NVS("VARS")
    
    while True:
        try:
            delay = nvs.get_i32("LED_DELAY") / 4
            print("current delay is "+str(delay))
            led.value(1)
            time.sleep(delay)
            led.value(0)
            time.sleep(delay)
            
        except:
            print("exception has ocurred on led_inter")
            exc_type = sys.exec_info()
            print(exc_type)
            break
    
            
        
        
        
    