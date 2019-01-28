# author: Sai Anjan
# task  : Object Oriented programming
# date  : 22/01/19

""" Write a Program DeckOfCards, to initialize deck of cards having suit ("Clubs", "Diamonds", "Hearts", "Spades")
    & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace").
    Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and
    Print the Cards the received by the 4 Players using 2D Array…
"""

import itertools
import random

# rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace']

# suit = ['clubs', 'diamonds', 'hearts', 'spades']


class Cards:                                        # This class is created for the deck_of_cards

    def deckofcards(self):
        """ This method is used to shuffle the deck of cards
            and distribute 9 card to each player
            total number of players are four.
        """
        """ This itertools module  standardizes a core set of fast, memory efficient tools that are 
            useful by themselves or in combination. Together, they form an “iterator algebra” making it possible 
            to construct specialized tools succinctly and efficiently in pure Python.
        """
        deck_of_cards = list(itertools.product(
            ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace'],
            ['clubs', 'diamonds', 'hearts', 'spades']))
        print(deck_of_cards)

        for number_of_players in range(1, 5):       # This loop shuffle cards to 4 players
            random.shuffle(deck_of_cards)           # "random.shuffle" is used to shuffle the cards
            print("\n")
            print("player = ", number_of_players, " got these cards \n")

            for number_of_cards in range(1, 10):    # This loop is to distribute 9 cards to the players
                print(number_of_cards, deck_of_cards[number_of_cards][0], " of ", deck_of_cards[number_of_cards][1])


Cards_object = Cards()                              # Card object is created


if __name__ == '__main__':
    Cards_object.deckofcards()                      # Deck of cards method is called


