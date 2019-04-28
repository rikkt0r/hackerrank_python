def rotate(arr, times):
    for _ in xrange(times):
        arr.append(arr.pop(0))
    print ' '.join([str(a) for a in arr])


if __name__ == '__main__':
    rotate([1, 2, 3, 4, 5], 1)
    rotate([1, 2, 3, 4, 5], 2)
    rotate([1, 2, 3, 4, 5], 6)
