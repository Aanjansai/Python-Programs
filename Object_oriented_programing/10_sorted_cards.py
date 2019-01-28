# author: Sai Anjan
# task  : Object Oriented programming
# date  : 26/01/19

""" Extend the above program to create a Player Object having Deck of Cards, and having ability to Sort by Rank
    and maintain the cards in a Queue implemented using Linked List. Do not use any Collection Library.
    Further the Player are also arranged in Queue. Finally Print the Player and the Cards received by each Player.
"""
# import itertools
# import random
#
#
# deck_of_cards = list(itertools.product(
#     ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace'],
#     ['clubs', 'diamonds', 'hearts', 'spades']))
# print(deck_of_cards)
#
# for number_of_players in range(1, 5):
#     random.shuffle(deck_of_cards)
#     print("\n")
#     print("player = ", number_of_players, " got these cards \n")
#
#     for number_of_cards in range(1, 10):
#         print(number_of_cards, deck_of_cards[number_of_cards][0], " of ", deck_of_cards[number_of_cards][1])


from enum import Enum
# enum is imported to set the named constant of distinct type


class Suit(Enum):            # enum super class is inherited by sub class suit
    Spade = 1
    Heart = 2
    Dimond = 3
    Club = 4

    def __str__(self):      # this method returns the name of the suit
        return self.name


class Rank(Enum):           # enum super class is inherited by sub class rank
    N1 = 1
    N2 = 2
    N3 = 3
    N4 = 4
    N5 = 5
    N6 = 6
    N7 = 7
    N8 = 8
    N9 = 9
    ace = 10
    Jack = 11
    Queen = 12
    King = 13

    def __str__(self):                  # method is overriding which returns the name
        if self.value <= 10:
            return str(self.value)
        return self.name


class Card:                  # this class is used to return the suit and rank number
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        return '{} {}'.format(self.suit, self.number)


cards = [Card(suit, number) for suit in Suit for number in Rank]  # list comprehension of cards

# this loop is to print the cards in sorted form
for card in cards:
    print(card)


















