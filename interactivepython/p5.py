# implementation of card game - Memory
import simplegui
import random

# helper function to initialize globals
def new_game():
    global nums, exposed, state, card1, card2, turn
    nums = range(8)
    nums.extend(nums)
    random.shuffle(nums)
    exposed = []
    for n in range(16):
        exposed.append(False)
    state=0
    card1 = 0
    card2 = 0
    turn = 0
    label.set_text("Turns = 0")

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, card1, card2, turn
    for n in range(16):
        if pos[0] >= n*50 and pos[0] < n*50 + 50:
            if exposed[n] == False:
                if state == 0:
                    exposed[n] = True
                    state = 1
                    card1 = n
                elif state == 1:
                    exposed[n] = True
                    state = 2
                    card2 = n
                    turn += 1
                    label.set_text("Turns = " + str(turn))
                else:
                    if nums[card1] != nums[card2]:
                        exposed[card1] = False
                        exposed[card2] = False
                    exposed[n] = True
                    state = 1
                    card1 = n 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global nums, exposed
    for n in range(16):
        if exposed[n] == False:
            canvas.draw_polyline([[n*50+25, 100], [n*50+25, 0]], 49, 'Green')
        else:
            canvas.draw_text(str(nums[n]), (n*50+11, 70), 60, 'White')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
