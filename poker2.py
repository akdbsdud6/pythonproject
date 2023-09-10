class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck(list):
    def __init__(self):
        suits = list(range(4))
        numbers = list(range(13))
        for i in suits:
            for j in numbers:
                self.append(Card(i, j))
    
    def printDeck(self):
        for i in self:
            if i.suit == 0:
                s = "Spades"
            elif i.suit == 1:
                s = "Hearts"
            elif i.suit == 2:
                s = "Diamonds"
            else:
                s = "Clubs"

            if i.number == 12:
                n = "A"
            elif i.number == 11:
                n = "K"
            elif i.number == 10:
                n = "Q"
            elif i.number == 9:
                n = "J"
            else:
                n = str(i.number + 2)

            print(n + " of " + s)
            
        

deck1 = Deck()
deck1.printDeck()

