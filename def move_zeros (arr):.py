def move_zeros (arr):
    return [x for x in arr if x != 0 or isinstance (x, bool)] + [x for x in arr if x ==0 and not isinstance (x, bool)]