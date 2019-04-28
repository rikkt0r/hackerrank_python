class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


def insertNodeAtHead(llist, data):
    if llist is None:
        return SinglyLinkedListNode(data)

    head = SinglyLinkedListNode(data)
    head.next = llist
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    for x in range(10):
        llist_head = insertNodeAtHead(llist.head, x)
        llist.head = llist_head

    printLinkedList(llist.head)
