#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    adds all unique integers in a list (only once for each integer)
    '''
    unique_set = set(my_list)
    result = 0
    # or this for num in set(my_list)

    for element in unique_set:
        result += element
    return result
