def removeDuplicates(head):
    tail = head
    while tail:
        if tail.next and tail.data == tail.next.data:
            tail.next = tail.next.next
        else:
            tail = tail.next
    return head
