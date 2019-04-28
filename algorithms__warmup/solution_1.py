def staircase(n):
    for x in range(1, n+1):
        print ('#' * x).rjust(n)


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
