#!/usr/bin/env python3
first = 1 # starting number
last = 105 # ending number (including)
substitutions = { # substitutions dictionary
    "fizz": 3,
    "buzz": 5,
    "cuzz": 7
    }

for i in range(first, last + 1):
    jn = True # print just number - neither fizz nor buzz

    for word, div in substitutions.items():
        # goes through key value pairs for substitution
        if not (i % div):
            print(word, end='')
            jn = False # set *not* to print the number
            
    print(i if jn else "") # newline or unsubstitued number
    
