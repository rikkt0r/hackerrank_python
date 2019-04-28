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
    print compareTriplets([1, 2, 3], [4, 5, 6])
    print compareTriplets([1, 2, 3], [4, 5, 3])
    print compareTriplets([55, 34, 3], [4, 999, 1])
