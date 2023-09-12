import random

class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        number_name = ""
        suit_name = ""

        if self.suit == 0:
            suit_name = "Spades"
        elif self.suit == 1:
            suit_name = "Hearts"
        elif self.suit == 2:
            suit_name = "Diamonds"
        #elif self.suit == 3:
            #suit_name = "Clubs"
        else:
            suit_name = "Clubs"
        
        if self.number == 12:
            number_name = "Ace"
        elif self.number == 11:
            number_name = "King"
        elif self.number == 10:
            number_name = "Queen"
        elif self.number == 9:
            number_name = "Jack"
        else:
            number_name = str(self.number+2)

        return number_name + " of " + suit_name

class Deck(list):
    def __init__(self):
        suits = list(range(4))
        numbers = list(range(13))
        for i in numbers:
            for j in suits:
                self.append(Card(j, i))

    def shuffle(self):
        random.shuffle(self)

    def deal(self, player):
        for i in range(0, 5):
            player.append(self.pop(0))

    def showdeck(self):
        for card in self:
            print(card)
            

deck1 = Deck()
deck1.showdeck()

