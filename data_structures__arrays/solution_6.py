def arrayManipulation(n, queries):
    # bruteforce and times out at some tests
    arr = [0] * n
    for q in queries:
        for i in xrange(q[0]-1, q[1]):
            arr[i] += q[2]

    return max(arr)


if __name__ == '__main__':
    print arrayManipulation(5, [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100],
    ])
