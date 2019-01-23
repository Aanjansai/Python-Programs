import itertools
import random

# rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace']

# suit = ['clubs', 'diamonds', 'hearts', 'spades']

deck_of_cards = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace'],
                                       ['clubs', 'diamonds', 'hearts', 'spades']))
print(deck_of_cards)

for number_of_players in range(1, 5):
    random.shuffle(deck_of_cards)
    print("\n")
    print("player = ", number_of_players, " got these cards \n")

    for number_of_cards in range(1, 10):
        print(number_of_cards, deck_of_cards[number_of_cards][0], " of ", deck_of_cards[number_of_cards][1])




