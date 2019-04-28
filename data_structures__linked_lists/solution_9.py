def getNode(head, positionFromTail):
    size = 0
    tail = head
    while tail is not None:
        size += 1
        tail = tail.next

    tail = head
    for x in range(size - positionFromTail - 1):
        tail = tail.next

    return tail.data
