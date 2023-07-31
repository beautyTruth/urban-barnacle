# Card class
# Suit, rank, value
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,
          'Queen':12,'King':13,'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # create the CARD object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # for a list of multiple card objects
            self.all_cards.extend(new_cards)
        else: 
            # for a single card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return "Player {} has {} cards".format(self.name,str(len(self.all_cards)))

# Game setup

player_one = Player('Luke')
player_two = Player('Vader')

new_deck = Deck()
new_deck.shuffle()

for dingleberry in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

# while game is on
round_num = 0

while game_on:
    round_num += 1
    print('Round {}'.format(round_num))
    
    if len(player_one.all_cards) == 0:
        print("Luke is out of cards! Darth Vader wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Vader is out of cards! Luke Skywalker wins!")
        game_on = False
        break

    # start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    # while at war
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war = False
            
        else:
            print('WAR!!!')
            
            if len(player_one.all_cards) < 5:
                print("Luke can't continue \nDarth Vader wins!")
                game_on = False
                break
                
            elif len(player_two.all_cards) < 5:
                print("Darth can't continue \nLuke Skywalker wins!")
                game_on = False
                break
                
            else:
                for peach in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())