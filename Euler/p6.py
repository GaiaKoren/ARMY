"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


"""


def sum_of_squares(limit):
    s = 0
    for i in range(limit+1):
        square = i ** 2
        s = s + square
    return s


def square_of_sum(limit):
    s = 0
    for i in range(limit+1):
        s = s + i
    return s**2


print(square_of_sum(100) - sum_of_squares(100))


