def miniMaxSum(arr):
    arr.sort()
    print '%d %d' % (sum(arr[:4]), sum(arr[1:]))


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
