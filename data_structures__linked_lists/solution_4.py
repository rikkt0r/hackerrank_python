# nonremovable __future__ import breaks python2. using py3

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def debug_print(head):
    current = head
    elems = []
    while current is not None:
        elems.append(str(current.data))
        current = current.next
    print (' --> '.join(elems))


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if head is None:
        return node
    tail = head
    if position == 0:
        node.next = tail
        return node

    for x in range(position-1):  # range(-int) == []
        tail = tail.next

    node.next = tail.next
    tail.next = node

    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    for x in range(10):
        llist.insert_node(x)

    debug_print(llist.head)

    llist_head = insertNodeAtPosition(llist.head, 123, 0)
    debug_print(llist_head)

    llist_head = insertNodeAtPosition(llist.head, 77, 1)
    debug_print(llist_head)

    llist_head = insertNodeAtPosition(llist_head, 567, 5)
    debug_print(llist_head)
