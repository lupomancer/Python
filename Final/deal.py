#! /usr/bin/env python3

import random
import cards
import pprint
from typing import List

def main():
    # Create a deck of cards
    deck = cards.make_deck()

    # Print deck
    print('\nDeck:')
    pprint.pprint(deck)

    # Randomize the order of the cards in the deck
    cards.shuffle_deck(deck)

    # Create a list of hands for 4 players with 13 cards in each hand
    hands = cards.deal_hands(4, 13, deck)

    # Print the hand for each player
    print('\nHands:')
    for player, hand in enumerate(hands):
        print('\nPlayer {}:  '.format(player))
        for card in hand:
            print('\t{}'.format(card))

    # Print all the cards of the heart suit in the players hands
    for i in range(13):
        if deck[i] == hands[i]:
                    print(hands[i])

if __name__ == '__main__':
    main()
