from machine import ADC, Pin, PWM
from time import sleep

led = PWM(Pin(2)) #defining led pin
potentiometer = ADC(Pin(28)) #defining potentiometer pin
led.freq(1000) #set the frequency

while True:
    value = potentiometer.read_u16() #getting potentiometer value
    print(value) #printing value to terminal
    led.duty_u16(value) #setting brightness of led
    sleep(0.2) #small delay for readability