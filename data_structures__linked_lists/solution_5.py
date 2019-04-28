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
    print ' --> '.join(elems)


def deleteNode(head, position):
    if position == 0:
        return head.next
    tail = head
    for x in range(position-1):
        tail = tail.next
    tail.next = tail.next.next
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    for x in range(10):
        llist.insert_node(x)

    head = llist.head
    debug_print(head)

    head = deleteNode(head, 0)
    debug_print(head)

    head = deleteNode(head, 0)
    debug_print(head)

    head = deleteNode(head, 7)
    debug_print(head)

