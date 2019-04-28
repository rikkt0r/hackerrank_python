def diagonalDifference(arr):
    _sum = 0
    n = len(arr)
    for i in xrange(n):
        _sum += arr[i][i]

    for i in xrange(n):
        _sum -= arr[n-i-1][i]

    return abs(_sum)


if __name__ == '__main__':
    test_data = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]

    print diagonalDifference(test_data)
