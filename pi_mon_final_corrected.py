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
    if not notFailed:
        return
    red.on()
    sleep(.25)
    red.off()
     
    if memory[index] == red:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False
         
def greenPressed():
    global index
    global notFailed
    if not notFailed:
        return
    green.on()
    sleep(.25)
    green.off()
     
    if memory[index] == green:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False
     
def redPressed():
    global index
    global notFailed
    if not notFailed:
        return
    red.on()
    sleep(.25)
    red.off()
     
    if memory[index] == red:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False     


def bluePressed():
    global index
    global notFailed
    if not notFailed:
        return
    blue.on()
    sleep(.25)
    blue.off()
     
    if memory[index] == blue:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False
         
def yellowPressed():
    global index
    global notFailed
    if not notFailed:
        return
    yellow.on()
    sleep(.25)
    yellow.off()
     
    if memory[index] == yellow:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False

user = input("enter 'y' to play...") #asks the user to play
if user == 'y':
    playing = True
else: playing = False

#this list will hold the ranomly selected leds to be pressed in order

memory =[]

while playing: #first loop allows multiple games to be played
    level = 0 #reset level indicator
    notFailed = True #Boolean to handle end of game

    while notFailed: #each iteration of this loop handles a level
        
        #increase level counter by one, then print current level (game will start at level 1)
        level += 1
        print("Begin level " + str(level))

        #turns all LEDs on, then turns them off

        for led in leds:
            led.on()
        sleep(.5)
        for led in leds:
            led.off()
        sleep(1)

        #generates a random integer from 0 to the length of 
        # the 'leds' list. The integer is usd to select an LED
        # and add it to the end of the 'memory' listpygame.examples.mask.main()

        randomLED = leds[randint(0,len(leds)-1)]
        memory.append(randomLED)
        #this for loop blinks each LED in 'memory' in order

        for led in memory:
            led.on()
            sleep(.25)
            led.off()
            sleep(.25)
        #'index' keeps track of our location in the 'memory' list
        #if the correct button is pressed, 'index' increases by one. (see functions above)

    
        index  = 0

        #this loop listend for a button to be pressed. Then it calls the associated function
        #that determines if the correct button was pressed and increases 'index'

        while index < len(memory) and notFailed:
            redB.when_pressed = redPressed
            greenB.when_pressed = greenPressed
            blueB.when_pressed = bluePressed
            yellowB.when_pressed = yellowPressed
    
    #game has ended. clear the list holding LED order, print final level, and ask to play again. 

    memory.clear()
    print("You made it to level " + str(level+1) + "!")
    user = input("enter 'y' to play again...")
     
    if user != 'y':
        playing = False
print("Goodbye!")


