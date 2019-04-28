def compare_lists(llist1, llist2):
    head = llist1
    head2 = llist2
    while head is not None and head2 is not None:
        if head.data != head2.data or (head.next is None)^(head2.next is None):
            return 0
        head = head.next
        head2 = head2.next
    return 1
