def equalStacks(h1, h2, h3):
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    idx1, idx2, idx3 = 0, 0, 0

    while sum1 != sum2 or sum2 != sum3:
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1[idx1]
            idx1 += 1

        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2[idx2]
            idx2 += 1

        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= h3[idx3]
            idx3 += 1

    return sum1


if __name__ == '__main__':
    # s1 = [3, 2, 1, 1, 1]
    # s2 = [4, 3, 2]
    # s3 = [1, 1, 4, 1]

    s1 = [1, 1, 1, 1, 2]
    s2 = [3, 7]
    s3 = [1, 3, 1]

    print(equalStacks(s1, s2, s3))
