def max_integer(my_list=[]):
    '''
    finds the biggest integer of a list
    '''
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_val:
            max_val = my_list[i]
    return max_val
