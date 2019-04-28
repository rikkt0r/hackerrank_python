# py2 doesn't work(linter errors), so paste this in py3
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
