def hourglassSum(arr):
    n = len(arr)
    s = None
    for i in xrange(n-2):
        for j in xrange(n - 2):
            tmp_s = sum(arr[i][j:j+3])
            tmp_s += sum(arr[i+2][j:j+3])
            tmp_s += arr[i+1][j+1]
            if s is None or s < tmp_s:
                s = tmp_s
    return s


if __name__ == '__main__':
    test_data = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    print hourglassSum(test_data)
