def staircase(n):
    for x in range(1, n+1):
        print ('#' * x).rjust(n)


if __name__ == '__main__':
    staircase(0)
    staircase(1)
    staircase(4)
    staircase(10)
