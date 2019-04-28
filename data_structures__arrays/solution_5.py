def matchingStrings(strings, queries):
    ret = []
    for query in queries:
        ret.append(strings.count(query))
    return ret

if __name__ == '__main__':
    strings = [
        'abcde',
        'sdaklfj',
        'asdjf',
        'na',
        'basdn',
        'sdaklfj',
        'asdjf',
        'na',
        'asdjf',
        'na',
        'basdn',
        'sdaklfj',
        'asdjf'
    ]
    queries = [
        'abcde',
        'sdaklfj',
        'asdjf',
        'na',
        'basdn'
    ]

    print matchingStrings(strings, queries)