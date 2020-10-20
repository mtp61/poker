import json
import random


RANKS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
SUITS = ['s', 'c', 'h', 'd']


def main():
    print(newDeck())
    r1_name = 'test'
    r2_name = 'test'

    # load the ranges
    with open('ranges.json', 'r') as f:
        ranges = json.loads(f.read())
        r1 = ranges[r1_name]
        r2 = ranges[r2_name]


'''
simulate a hand with starting hands h1 and h2]
returns 1 if h1 wins, 0 otherwise
'''
def simulateHand(h1, h2):
    # get a deck
    d = newDeck()

    # remove starting hands from the deck
    d.remove(h1)
    d.remove(h2)
    
    # pick 5 cards from the deck
    community_cards = d[:5]


'''
returns a shuffled deck
'''
def newDeck():
    d = []
    for r in RANKS:
        for s in SUITS:
            d.append(f'{r}{s}')
    random.shuffle(d)
    return d


if __name__ == '__main__':
    main()
