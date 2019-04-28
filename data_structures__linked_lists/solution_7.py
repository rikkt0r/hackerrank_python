def reverse(head):
    if head.next is None:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
