import os


def diagonalDifference(arr):
    _sum = 0
    n = len(arr)
    for i in xrange(n):
        _sum += arr[i][i]

    for i in xrange(n):
        _sum -= arr[n-i-1][i]

    return abs(_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
