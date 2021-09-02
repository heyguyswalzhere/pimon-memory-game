from random import randint #allows LEDs to turn on randomly
from gpiozero import LED, Button #manages buttons and LEDS
from time import sleep #allows program to pause

red = LED(21)
green = LED(10)
blue = LED (11)
yellow = LED(17)

#list containing all of the LEDs
leds = [red, green, blue, yellow]

redB = Button(13)  #assigns buttons to GPIO pins
greenB = Button(5)
blueB = Button(27)
yellowB = Button(2)

#the following functions handle button presses
#the pressed button blinks. If it was the correct
#button, a "Correct!" message is printed and the
# index in increased. Otherwise "Incorrect!" is
#printed and the "notFailed" boolean is set to
# false, ending the game.

def redPressed():
     global index
     global notFailed
     
     red.on()
     sleep(.25)
     red.off()
     
     if memory[index] == red:
         print("Correct!")
         index += 1
     else:
         print("Incorrect!")
         notFailed == False
         
def greenPressed():
     global index
     global notFailed
     
     green.on()
     sleep(.25)
     green.off()
     
     if memory[index] == green:
         print("Correct!")
         index += 1
     else:
         print("Incorrect!")
         notFailed == False
     
def redPressed():
     global index
     global notFailed
     
     red.on()
     sleep(.25)
     red.off()
     
     if memory[index] == red:
         print("Correct!")
         index += 1
     else:
         print("Incorrect!")
         notFailed == False     


def bluePressed():
     global index
     global notFailed
     
     blue.on()
     sleep(.25)
     blue.off()
     
     if memory[index] == blue:
         print("Correct!")
         index += 1
     else:
         print("Incorrect!")
         notFailed == False
         
def yellowPressed():
     global index
     global notFailed
     
     yellow.on()
     sleep(.25)
     yellow.off()
     
     if memory[index] == yellow:
         print("Correct!")
         index += 1
     else:
         print("Incorrect!")
         notFailed == False