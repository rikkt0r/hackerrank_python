from decimal import Decimal


def plusMinus(arr):
    n = len(arr)
    plus = Decimal(len(filter(lambda x: x > 0, arr))) / n
    minus = Decimal(len(filter(lambda x: x < 0, arr))) / n
    zero = Decimal(len(filter(lambda x: x == 0, arr))) / n

    print '%.6f\n%.6f\n%.6f' % (plus, minus, zero)


if __name__ == '__main__':
    plusMinus([1, 2, 3, -4, 0, 0, 0, 0, -3, -2, 1, 4])
