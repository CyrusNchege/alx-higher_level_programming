#!/usr/bin/python3
def islower(c):
    '''
    CHecks whether charcater chr() passed to it is lowercase or uppercaase
    '''
    # check if the ASCII code for c is within the range of lowercase letters
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
