#!/usr/bin/python3
'''
MyList that inherits from list
'''


class MyList(list):
    '''
    List object
    Methods:
        print_sorted: Prints a sorted list
    '''

    def print_sorted(self):
        '''
        Prints a sorted list
        '''
        print(sorted(self))
