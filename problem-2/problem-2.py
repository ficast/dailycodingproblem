import math


def product_array1(array):
    return_array = []

    for number in array:
        temp_array = list(array)
        temp_array.remove(number)
        return_array.append(math.prod(temp_array))

    return return_array


def product_array2(array):
    return_array = []

    for number in array:
        temp_array = list(array)
        temp_array.remove(number)
        product = 1

        for num in temp_array:
            product *= num
        return_array.append(product)

    return return_array


def product_array3(array):
    """ In this solution array must not contain zeros '0' """
    return_array = []
    product = 1

    for num in array:
        product *= num

    for number in array:
        return_array.append(product/number)

    return return_array


assert product_array1([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_array1([3, 2, 1]) == [2, 3, 6]
assert product_array2([0, 1, 2]) == [2, 0, 0]
assert product_array2([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_array2([3, 2, 1]) == [2, 3, 6]
assert product_array2([0, 1, 2]) == [2, 0, 0]
assert product_array3([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_array3([3, 2, 1]) == [2, 3, 6]
assert product_array3([1, 1, 2]) == [2, 2, 1]
