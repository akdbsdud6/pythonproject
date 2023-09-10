
import random

def draw_hand(deck):
    hand = random.sample(deck, k=5)
    print("Your hand:", hand)
    ans = -99
    to_change = []
    while ans != -1:
        ans = int(input("Type the index of the card you want to change (0 for none / stop, 1 for first, and so on)\n >>> ")) - 1
        if ans != -1 and ans not in to_change:
            to_change.append(ans)
        print("\n")
    print("\n\n\n\n\n\n")
    num = len(to_change)
    if num != 0:
        while len(to_change) != 0:
            index = to_change.pop(to_change.index(max(to_change)))
            hand.pop(index)
        new_draw = random.sample(deck, num)
        hand += new_draw
    return hand
    

    
    


def main():
    spades = ["A spades", "2 spades", "3 spades", "4 spades", "5 spades", "6 spades", "7 spades", "8 spades", "9 spades", "10 spades", "J spades", "Q spades", "K spades"]
    hearts = ["A hearts", "2 hearts", "3 hearts", "4 hearts", "5 hearts", "6 hearts", "7 hearts", "8 hearts", "9 hearts", "10 hearts", "J hearts", "Q hearts", "K hearts"]
    diamonds = ["A diamonds", "2 diamonds", "3 diamonds", "4 diamonds", "5 diamonds", "6 diamonds", "7 diamonds", "8 diamonds", "9 diamonds", "10 diamonds", "J diamonds", "Q diamonds", "K diamonds"]
    clubs = ["A clubs", "2 clubs", "3 clubs", "4 clubs", "5 clubs", "6 clubs", "7 clubs", "8 clubs", "9 clubs", "10 clubs", "J clubs", "Q clubs", "K clubs"]
    deck = ["joker"] + spades + hearts + diamonds + clubs


    temp = deck
    hand1 = draw_hand(temp)
    hand2 = draw_hand(deck)

    print("final hand of player 1:", hand1)
    print("\n\n")
    print("final hand of player 2:", hand2)



        





    
if __name__ == "__main__":
    main()