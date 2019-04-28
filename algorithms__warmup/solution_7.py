def birthdayCakeCandles(ar):
    m = max(ar)
    return ar.count(m)


if __name__ == '__main__':
    print birthdayCakeCandles([4, 4, 2, 3])
