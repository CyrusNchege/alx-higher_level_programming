def max_integer(my_list=[]):
    '''
    finds the biggest integer of a list
    '''
    if len(my_list) == 0:
        return None

    max_val = my_list[0]
    for i in my_list:
        if max_val < i:
            max_val = i
    return max_val
