# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables
num_range = 100
num = random.randrange(0, 100)
count = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range 
    global num
    global count
    if num_range == 100: 
        count = 7
    else: 
        count = 10
    print "New Game. Range is from 0 to", num_range
    print "Number of remaining guesses is", count, "\n"
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range 
    global num
    num_range = 100
    new_game()
    num = random.randrange(0, 100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range 
    global num
    num_range = 1000
    new_game()
    num = random.randrange(0, 1000)
    
def input_guess(guess):
    # main game logic goes here
    global num_range 
    global num
    global count
    guess = int(guess)
    count -= 1
    print "guess was", guess
    print "Number of remaining guesses is", count
    if num > guess:
        if count > 0:
            print "Higher!", "\n"
        else:
            print "You ran out of guesses. The number was", num, "\n"
            new_game()
    elif num < guess:
        if count > 0:
            print "Lower!", "\n"
        else:
            print "You ran out of guesses. The number was", num, "\n"
            new_game()
    else:
        print "Correct!", "\n"
        new_game()
       

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
