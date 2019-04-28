#!/bin/python

import os


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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    res = findLonely(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
