# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0.0, 0.0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global start
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 4)
    elif direction == LEFT:
        ball_vel[0] = - random.randrange(2, 4)
    ball_vel[1] = - random.randrange(1, 3)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # determine whether paddle and ball collide and update ball
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] <= paddle1_pos + PAD_HEIGHT/2 and ball_pos[1] >= paddle1_pos - PAD_HEIGHT/2:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] <= paddle2_pos + PAD_HEIGHT/2 and ball_pos[1] >= paddle2_pos - PAD_HEIGHT/2:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            spawn_ball(LEFT)
            score1 += 1
        
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # draw ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "Red")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel > PAD_HEIGHT/2 and paddle1_pos + paddle1_vel < HEIGHT - PAD_HEIGHT/2:
        paddle1_pos += paddle1_vel
    if paddle1_pos + paddle1_vel <= PAD_HEIGHT/2:
        paddle1_pos = PAD_HEIGHT/2
    if paddle1_pos + paddle1_vel >= HEIGHT - PAD_HEIGHT/2:
        paddle1_pos = HEIGHT - PAD_HEIGHT/2
    if paddle2_pos + paddle2_vel > PAD_HEIGHT/2 and paddle2_pos + paddle2_vel < HEIGHT - PAD_HEIGHT/2:
        paddle2_pos += paddle2_vel
    if paddle2_pos + paddle2_vel <= PAD_HEIGHT/2:
        paddle2_pos = PAD_HEIGHT/2
    if paddle2_pos + paddle2_vel >= HEIGHT - PAD_HEIGHT/2:
        paddle2_pos = HEIGHT - PAD_HEIGHT/2
    
    # draw paddles
    if paddle1_pos == PAD_HEIGHT/2:
        canvas.draw_polyline([[HALF_PAD_WIDTH, PAD_HEIGHT], [HALF_PAD_WIDTH, 0]], PAD_WIDTH, 'Red')
    elif paddle1_pos == HEIGHT - PAD_HEIGHT/2:
        canvas.draw_polyline([[HALF_PAD_WIDTH, HEIGHT - PAD_HEIGHT], [HALF_PAD_WIDTH, HEIGHT]], PAD_WIDTH, 'Red')
    else:
        canvas.draw_polyline([[HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT/2], [HALF_PAD_WIDTH, paddle1_pos - PAD_HEIGHT/2]], PAD_WIDTH, 'Blue')
    
    if paddle2_pos == PAD_HEIGHT/2:
        canvas.draw_polyline([[WIDTH - HALF_PAD_WIDTH, PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, 0]], PAD_WIDTH, 'Red')
    elif paddle2_pos == HEIGHT - PAD_HEIGHT/2:
        canvas.draw_polyline([[WIDTH - HALF_PAD_WIDTH, HEIGHT - PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, HEIGHT]], PAD_WIDTH, 'Red')
    else:
        canvas.draw_polyline([[WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT/2], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - PAD_HEIGHT/2]], PAD_WIDTH, 'Blue')
    
    # draw scores
    canvas.draw_text(str(score1), [230, 100], 36, "Green")
    canvas.draw_text(str(score2), [350, 100], 36, "Greeen")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    if key==simplegui.KEY_MAP["s"]:
        #paddle1_vel -= acc
        paddle1_vel = paddle_vel
    elif key==simplegui.KEY_MAP["w"]:
        #paddle1_vel += acc
        paddle1_vel = - paddle_vel
    if key==simplegui.KEY_MAP["down"]:
        #paddle2_vel += acc
        paddle2_vel = paddle_vel
    elif key==simplegui.KEY_MAP["up"]:
        #paddle2_vel -= acc
        paddle2_vel = - paddle_vel
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Restart", new_game, 100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
