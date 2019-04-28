from decimal import Decimal


def plusMinus(n, arr):
    plus = Decimal(len(filter(lambda x: x > 0, arr))) / n
    minus = Decimal(len(filter(lambda x: x < 0, arr))) / n
    zero = Decimal(len(filter(lambda x: x == 0, arr))) / n

    print '%.6f\n%.6f\n%.6f' % (plus, minus, zero)

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(n, arr)
