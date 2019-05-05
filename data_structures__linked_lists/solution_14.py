class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


def to_str(head):
    # better lookup for test data :P
    data = []
    while head:
        data.append(str(head.data))
        head = head.next
    return ', '.join(data)


def sortedInsert(head, data):
    if head is None:
        return DoublyLinkedListNode(data)

    current = head
    prev = None

    while current and current.data < data:
        prev = current
        current = current.next

    new = DoublyLinkedListNode(data)
    new.next = current
    if prev:
        prev.next = new
        return head
    return new


if __name__ == '__main__':
    h = DoublyLinkedListNode(0)
    h_current = h
    for x in range(1, 11):
        n = DoublyLinkedListNode(x*2)
        n.prev = h_current
        h_current.next = n
        h_current = n

    print(to_str(h))

    h = sortedInsert(h, -2)
    print(to_str(h))

    h = sortedInsert(h, 5)
    print(to_str(h))

    h = sortedInsert(h, 6)
    print(to_str(h))

    h = sortedInsert(h, 7)
    print(to_str(h))

    h = sortedInsert(h, 99)
    print(to_str(h))
