import unittest
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
    result = []
    size = len(array)

    for i, _ in enumerate(array):
        product = 1
        for _num in array[0:i] + array[i+1:size]:
            if not isinstance(_num, (int, float)):
                raise TypeError
            product *= _num
        result.append(product)
    return result


assert product_array1([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_array1([3, 2, 1]) == [2, 3, 6]
assert product_array2([0, 1, 2]) == [2, 0, 0]
assert product_array2([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_array2([3, 2, 1]) == [2, 3, 6]
assert product_array2([0, 1, 2]) == [2, 0, 0]
assert product_array3([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_array3([3, 2, 1]) == [2, 3, 6]
assert product_array3([0, 1, 2]) == [2, 0, 0]
assert product_array3([0, 0, 0]) == [0, 0, 0]


class MyTestCase(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(TypeError, product_array3, ['0', 0, 0])

    def test_result_with_zeros(self):
        self.assertEqual(product_array3([0, 0, 0]), [0, 0, 0])

    def test_with_values(self):
        self.assertEqual(product_array3(
            [1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(product_array3([3, 2, 1]), [2, 3, 6])


if __name__ == '__main__':
    unittest.main()
