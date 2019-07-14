def contains_item(L, s):

    for item in L:
        if item == s:
            return True
        else:
            return False


print (contains_item([], 1))