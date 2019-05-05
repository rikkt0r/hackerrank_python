class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


def to_str(head):
    data = []
    while head:
        data.append(str(head.data))
        head = head.next
    return ', '.join(data)


def reverse_recursive(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_recursive(head.next)
    new_head.prev = head
    head.next.next = head
    head.next = None
    return new_head


def reverse_iterative(head):
    if head is None or head.next is None:
        return head

    current = head

    new_head = DoublyLinkedListNode(current.data)
    new_head_start = new_head
    current = current.next

    while current:
        new = DoublyLinkedListNode(current.data)
        new.prev = new_head
        new_head.next = new
        new_head = new

        current = current.next

    return new_head_start


if __name__ == '__main__':
    h = DoublyLinkedListNode(0)
    h_current = h
    for x in range(1, 11):
        n = DoublyLinkedListNode(x*2)
        n.prev = h_current
        h_current.next = n
        h_current = n

    print(to_str(h))

    h = reverse_iterative(h)
    print(to_str(h))
