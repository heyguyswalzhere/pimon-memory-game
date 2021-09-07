from gpiozero import LED
from time import sleep
from random import randint

def all_flash(): #a function that flashes all four LEDs
    red.on()
    blue.on()
    yellow.on()
    green.on()
    sleep(.5)
    red.off()
    blue.off()
    green.off()
    yellow.off()
    sleep(.5)
        
red = LED(21)
yellow = LED(17)
blue = LED(11)
green = LED(10) #these just assign LEDs to GPIO pins
        
lights = [] #initializes an empty list
        
while True:
    new = randint(1,4)
    lights.append(new)
    
    for light in lights:
        if light == 1:
            red.on()
            sleep(.25)
            red.off()
            sleep(.3)
       
        elif light == 2:
            yellow.on()
            sleep(.25)
            yellow.off()
            sleep(.3) 
       
        elif light == 3:
            blue.on()
            sleep(.25)
            blue.off()
            sleep(.3)
       
        elif light == 4:
            green.on()
            sleep(.25)
            green.off()
            sleep(.3)
        else:
            print:("ERROR!")#catches errors for the LEDs turning on 
            break
    
    all_flash()
    print(len(lights))
            

            

            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
