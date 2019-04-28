def findLonely(arr):
    res = arr[0]
    for idx in range(1, len(arr)):
        res ^= arr[idx]
    return res

def findLonelyCounter(arr):
    from collections import Counter
    c = Counter(arr)
    for k, count in c.items():
        if count == 1:
            return k


if __name__ == '__main__':
    print findLonely([1, 2, 2, 3, 3, 4, 4])
    print findLonely([5, 5, 2, 2, 7, 8, 8, 5, 5])
