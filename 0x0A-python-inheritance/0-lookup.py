#!/usr/bin/python3
'''
Module contains lookup function
'''

def lookup(obj):
    '''
    Returns the list of available attributes and methods of an object.
    args:
         obj (object): The object whose attributes and methods
    '''
    return dir(obj)
