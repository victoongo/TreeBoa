# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
time = 0
score = 0
n_of_clicks = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    decisec = t % 10
    sec = (t // 10) % 60
    if sec < 10:
        sec = "0" + str(sec)
    else:
        sec = str(sec)
    min = (t // 10) // 60
    return str(min) + ":" + sec + "." + str(decisec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global n_of_clicks
    global score
    if timer.is_running() == 1:
        n_of_clicks += 1
        timer.stop()
        if time % 10 == 0:
            score += 1

def reset():
    global time
    global n_of_clicks
    global score
    timer.stop()
    time = 0
    score = 0
    n_of_clicks = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    if timer.is_running() == 1:
        time += 1
        #print time

# define draw handler
def draw(canvas):
    score_board = str(str(score) + "/" + str(n_of_clicks))
    canvas.draw_text(format(time), [45, 70], 30, "White")
    canvas.draw_text(score_board, [120, 20], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 150, 120)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()
#timer.start()
