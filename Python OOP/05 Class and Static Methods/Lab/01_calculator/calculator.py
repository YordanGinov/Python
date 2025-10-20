from functools import reduce


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(*numbers):
        return sum(numbers)

    @staticmethod
    def multiply(*numbers):
    #     mult = 0
    #     for number in numbers:
    #         if mult == 0:
    #             mult = number
    #         else:
    #             mult *= number
    #     return mult
        return reduce(lambda x, y: x * y, numbers)

    @staticmethod
    def divide(*numbers):
        # div = 0
        # for number in numbers:
        #     if div == 0:
        #         div = number
        #     else:
        #         div = div / number
        # return div
        return reduce(lambda x, y: x / y, numbers)

    @staticmethod
    def subtract(*numbers):
        # subtract = 0
        # for number in numbers:
        #     if subtract == 0:
        #         subtract = number
        #     else:
        #         subtract -= number
        # return subtract
        return reduce(lambda x, y: x - y, numbers)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
