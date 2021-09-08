# pimon-memory-game
This game should play like this: 
the user clicks y to play
all lights flash
the patter is displayed
the user repeats the pattern
if correct: all lights flash and a new pattern is given
if incorrect: shell outputs level status and asks for user input to play again
Here is the trouble shooting we had to do with the "final code": 
1. look for two red.Pressed functions. This won't break the code, but it's...wrong. 
2. Look at notFailed. Are there two equal signs? There should only be one. 
3. The indent was off. Your assistant should tell you if there are indents that need to be fixed. 
4. for each defcolorPressed(): function we added
if not notFailed:
  return
 That function should allow the loop to go back to the top and continue the game. 
                                                
