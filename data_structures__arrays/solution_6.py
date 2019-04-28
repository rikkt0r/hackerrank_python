def arrayManipulationBruteForce(n, queries):
    # times out some tests
    arr = [0] * n
    for q in queries:
        for i in xrange(q[0]-1, q[1]):
            arr[i] += q[2]

    return max(arr)


def arrayManipulation(n, queries):
    # based on discussions on the topic
    arr = [0] * (n+2)
    for i, j, val in queries:
        arr[i] += val
        if j+1 <= n:
            arr[j+1] -= val

    tmp, mx = 0, 0
    for i in xrange(1, n+1):
        tmp += arr[i]
        if mx < tmp:
            mx = tmp

    return mx


if __name__ == '__main__':
    print arrayManipulation(5, [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100],
    ])
