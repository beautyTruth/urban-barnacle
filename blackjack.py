
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,
         'Queen':10,'King':10,'Ace':11}

playing = True

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
            
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck():
    
    def __init__(self):
        self.deck = []
        for peach in suits:
            for cherry in ranks:
                self.deck.append(Card(peach,cherry))
                
    def __str__(self):
        deck_composition = ''
        for dingleberry in self.deck:
            deck_composition += '\n' + dingleberry.__str__()
        return "The deck has: " + deck_composition
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand():
    
    def __init__(self):
        self.cards = [] # start with an empty list as we did in the deck class
        self.value = 0 # start with a zero value
        self.aces = 0 # add an attribute to keep track of aces
        
    def add_card(self,card):
        # card is passed in from Deck.deal() -- single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        # track the aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        # if the player's total value > 21 and they still have an ace
        # then change the ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    def __init__(self,total=100):
        self.total = total  # This can be set to any default value or supplied by user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        
        try: 
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips and you are a terrible person. You only have {} chips".format(chips.total))
            else:
                break
            
def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s ') 
        
        # account for typos like H or stand or HIT etc
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player stands; dealer's turn")
            playing = False
            
        else:
            print("Sorry, I didn't understand what you typed. Please enter an h or an s.")
            continue
            
        break

# Write functions to display the cards

def show_some(player,dealer):
    
    # show only one of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card is hidden!")
    print(dealer.cards[1])
    
    # show all (2 cards) of the player's hand/cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    
    
def show_all(player,dealer):
    
    # show all of the dealer's cards
    
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    
    # calculate and display the value (example Jack + King == 20)
    
    print("Value of dealer's hand is: {}".format(dealer.value))
    
    # show all of the player's cards
    
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
        
    print("Value of player's hand is: {}".format(player.value))

def player_busts(player,dealer,chips):
    print('Player BUSTS!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player WINS!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer BUST!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer WINS!')
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tie! PUSH!")

while True:
    
    # print an opening statement
    
    print("Welcome to the Glen Avenue Casino blackjack table")
    # create and shuffle a deck, two cards to each player
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the player's chips
    
    player_chips = Chips()
    
    # Prompt the player for their bet
    
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # prompt the player to hit or stand
        
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one of the dealer's cards hidden)
        
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of the loop
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            
            break
            
    # if the player hasn't busted, play dealer's hand until dealer reaches 17
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
        
        # show all cards
        
        show_all(player_hand,dealer_hand)
        
        # run different winning scenarios
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    # inform the player of their chips total
    
    print('\n Player total chips are at: {}'.format(player_chips.total))
    
    # ask to play again
    
    new_game = input("Would you like to play another hand, you degenerate gambler? y/n")
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Good. This is the first step in conquering your gambling addiction')
        break