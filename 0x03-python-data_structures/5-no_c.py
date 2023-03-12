#!/usr/bin/env python3
def no_c(my_string):
    '''
    removes all characters c and C from a string
    '''
    return(my_string.translate({ord('C'): None, ord('c'): None}))
