def list_add_up_to(array, k):
    for i in array:
        diff = k - i
        array.remove(i)
        if diff in array:
            return True
    return False


assert list_add_up_to([10, 15, 3, 7], 17) == True
assert list_add_up_to([10, 15, 20, 25, 30, 35, 40], 40) == True
assert list_add_up_to([0, 15, 3, 0], 0) == True
assert list_add_up_to([1, 15, 3, 0], 0) == False
assert list_add_up_to([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 17) == True
