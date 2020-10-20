import json


RANKS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def main():
    # store the range in a list
    r = emptyRange()

    # main loop
    while True:
        i = input('add a hand or type "save" to save the range: ').upper()
        if len(i) == 3:
            i = i[:2] + i[2].lower()

        if i == "SAVE":
            break
        elif not checkHand(i):
            print(f'"{i}" is not a valid hand"')
        else:
            rangeAdd(r, i)
    
    name = input('enter a name for the range: ')
    print(f'saving the following range as "{name}"')
    printRange(r)

    with open('ranges.json', 'r') as f:
        ranges = json.loads(f.read())

    ranges[name] = r

    with open('ranges.json', 'w') as f:
        f.write(json.dumps(ranges))
        

'''
returns an empty range
'''
def emptyRange():
    r = []
    for _ in range(13):
        r.append([0] * 13)
    return r


'''
returns a full range
'''
def fullRange():
    r = []
    for _ in range(13):
        r.append([1] * 13)
    return r


'''
returns 1 if a valid hand, 0 otherwise
'''
def checkHand(h):
    if len(h) == 2:
        if h[0] in RANKS and h[1] in RANKS:
            return 1
    elif len(h) == 3:
        if h[0] in RANKS and h[1] in RANKS and (h[2] == 's' or h[2] == 'o'):
            return 1
    return 0


'''
adds a starting hand 
'''
def rangeAdd(r, h):
    if len(h) == 3 and h[2] == 's':  # if suited
        i = RANKS.index(h[0])
        j = RANKS.index(h[1])
    else:
        i = RANKS.index(h[1])
        j = RANKS.index(h[0])
    r[i][j] = 1


'''
prints the range with nice formatting
'''
def printRange(r):
    print('    ', end='')
    for c in RANKS:
        print(f'{c}   ', end='')
    print()

    for i, c1 in enumerate(RANKS):
        print(f'{c1}   ', end='')
        for j, c2 in enumerate(RANKS):
            if r[i][j]:
                if j > i:
                    print(f'{c1}{c2}s ', end='')
                else:
                    print(f'{c2}{c1}  ', end='')
            else:
                print('    ', end='')
        print()


if __name__ == '__main__':
    main()
