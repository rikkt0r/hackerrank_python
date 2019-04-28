import os


def compareTripletsFancyMoreOps(a, b):
    compare = lambda x, y: 0 if x==y or y>x else 1
    alice = 0
    bob = 0
    for idx in range(len(a)):
        alice += compare(a[idx], b[idx])
        bob += compare(b[idx], a[idx])
    return [alice, bob]


def compareTriplets(a, b):
    alice = 0
    bob = 0
    for idx in range(len(a)):
        if a[idx] > b[idx]:
            alice += 1
        elif b[idx] > a[idx]:
            bob += 1
    return [alice, bob]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
