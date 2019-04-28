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


def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    tail = head
    while True:
        if tail.next is None:
            break
        tail = tail.next
    tail.next = SinglyLinkedListNode(data)
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    for x in range(10):
        llist_head = insertNodeAtTail(llist.head, x)
        llist.head = llist_head

    printLinkedList(llist.head)
