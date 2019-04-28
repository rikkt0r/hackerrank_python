def get_size(head):
    size = 0
    while head:
        head = head.next
        size += 1
    return size


def to_str(head):
    # better lookup for test data :P
    data = []
    while head:
        data.append(str(head.data))
        head = head.next
    return ', '.join(data)


def findMergeNode(head1, head2):
    # return '%s // %s' % (
    #     to_str(head1),
    #     to_str(head2),
    # )

    size1 = get_size(head1)
    size2 = get_size(head2)

    if size1 > size2:
        llarger, lsmaller = head1, head2
    else:
        llarger, lsmaller = head2, head1

    size_diff = abs(size1 - size2)
    for _ in range(size_diff):
        llarger = llarger.next

    while llarger and lsmaller:
        if llarger == lsmaller:
            return llarger.data

        llarger = llarger.next
        lsmaller = lsmaller.next

    return None
