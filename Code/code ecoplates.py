import machine
from time import sleep_ms, ticks_ms
from machine import Pin


button = machine.Pin(14,machine.Pin.IN, machine.Pin.PULL_DOWN)
Ci = machine.Pin(16,machine.Pin.OUT)
CiT = machine.Pin(17,machine.Pin.OUT)
CiPC = machine.Pin(15,machine.Pin.OUT)
led = Pin(25, Pin.OUT)
paso = 0

while True:
    paso = 1
    if paso == 1:
        Ci.value(1)
        CiT.value(1)
        CiPC.value(1)
        led.value(1)
        sleep_ms(5000)
        led.value(0)
        sleep_ms(2000)
        
        led.value(1)
        Ci.value(1)
        CiT.value(0)
        CiPC.value(1)
        led.value(0)
        sleep_ms(3000)

        print("tamizado")
     
        
        led.value(1)
        CiPC.value(1)
        CiT.value(1)
        sleep_ms(3000)
        Ci.value(0)
        led.value(0)
        sleep_ms(1000)   
        print("paso")
        
        led.value(1)
        Ci.value(1)
        CiT.value(1)
        sleep_ms(1000)
        CiPC.value(0)
        led.value(0)
        sleep_ms(2000) 
        print("prensado/cortado")
        paso = 0 
