from collections import defaultdict


def dynamicArray(n, queries):
    arr = defaultdict(list)
    last = 0
    lasts = []

    for query in queries:
        idx = (query[1] ^ last) % n
        if query[0] == 1:
            arr[idx].append(query[2])

        if query[0] == 2:
            last = arr[idx][query[2] % len(arr[idx])]
            lasts.append(last)

    return lasts


if __name__ == '__main__':
    result = dynamicArray(2, [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ])
    print '\n'.join(map(str, result))

