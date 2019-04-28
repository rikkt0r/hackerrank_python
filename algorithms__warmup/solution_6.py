def timeConversion(s):
    # 12:00 PM == 12:00
    # 12:00 AM == 00:00
    tt = s[-2:]
    t = s[:-2]
    hours = int(t[:2])
    rest = t[2:]

    if tt == 'AM':
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12

    return '%s%s' % (
        str(hours).zfill(2),
        rest
    )


if __name__ == '__main__':
    print timeConversion('12:03:11PM')
    print timeConversion('12:03:11AM')
    print timeConversion('7:03:11PM')
    print timeConversion('7:03:11AM')
