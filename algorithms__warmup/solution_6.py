import os


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
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
