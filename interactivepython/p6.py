# Mini-project #6 - Blackjack
import simplegui
import random
# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        if len(self.hand) > 0:
            for i in range(len(self.hand)):
                ans += str(self.hand[i]) + " "
        return ans

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)
        return self.hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        ans = 0
        acount = 0
        if len(self.hand) > 0:
            for i in range(len(self.hand)):
                ans += VALUES[self.hand[i].get_rank()]
                if self.hand[i].get_rank() == "A":
                    #if acount > 0 and ans + 10 <= 21:
                    #    ans += 10
                    acount += 1
            if acount > 0 and ans + 10 <= 21:
                ans += 10
        return ans
   
    def draw(self, canvas, y):
        # draw a hand on the canvas, use the draw method for cards
            #for i in range(len(dealer)):
        for i in range(len(self.hand)):
            x = 50 + i*80
            self.hand[i].draw(canvas, [x, y])

# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                c = Card(s, r)
                self.deck.append(c)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        #pass

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0)
        
    def __str__(self):
        # return a string representing the deck
        ans = ""
        if len(self.deck) > 0:
            for i in range(len(self.deck)):
                ans += str(self.deck[i]) + " "
        return ans

#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, deck, outcome, score
    
    if in_play == True:
        score -= 1
    
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    # your code goes here
    #print "dealer:",dealer
    #print "player:", player
    in_play = True
    outcome = "Hit or stand?"

def hit():
    global score, in_play, dealer, player, deck, outcome
    # replace with your code below
 
    # if the hand is in play, hit the player
    
    # if busted, assign a message to outcome, update in_play and score
    if in_play == True and player.get_value() <= 21:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = "you are busted! New deal?"
            score -= 1
            in_play = False
    print player.get_value()
    
def stand():
    global score, in_play, dealer, player, deck, outcome
    # replace with your code below
    if player.get_value() > 21:
            outcome = "you are busted! New deal?"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "dealer is busted! New deal?"
            score += 1
            in_play = False
        elif dealer.get_value() >= player.get_value():
            outcome = "dealer won! New deal?"
            score -= 1
            in_play = False
        else:
            outcome = "player won! New deal?"
            score += 1
            in_play = False
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global score, in_play, dealer, player, outcome
    # test to make sure that card.draw works, replace with your code below
    #score_board = str(str(score) + "/" + str(n_of_clicks))
    canvas.draw_text("Blackjack", [60, 60], 50, "White")
    canvas.draw_text("Score: ", [300, 60], 40, "Black")
    canvas.draw_text(str(score), [440, 60], 40, "Black")
    canvas.draw_text("Dealer", [60, 150], 40, "Black")
    canvas.draw_text("Player", [60, 350], 40, "Black")
    canvas.draw_text(outcome, [60, 560], 40, "Red")
    dealer.draw(canvas, 190)
    player.draw(canvas, 390)
    if in_play == True:
        canvas.draw_image(card_back, [36, 48], [72, 96], [50+36, 190+48], [72, 96])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling  
deal()
frame.start()