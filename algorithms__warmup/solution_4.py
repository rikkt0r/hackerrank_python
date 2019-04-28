def miniMaxSum(arr):
    arr.sort()
    print '%d %d' % (sum(arr[:4]), sum(arr[1:]))


if __name__ == '__main__':
    print miniMaxSum([1, 2, 3, 4, 5])
    print miniMaxSum([5, 4, 3, 2, 1])
