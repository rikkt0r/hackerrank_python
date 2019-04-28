def mergeLists(head1, head2):
    new = None
    new_head = None
    while head1 or head2:
        if head1 and head2 and head1.data <= head2.data or head1 and not head2:
            n = SinglyLinkedListNode(head1.data)
            head1 = head1.next

        else:
            n = SinglyLinkedListNode(head2.data)
            head2 = head2.next

        if new_head is None:
            new_head = new = n
        else:
            new.next = n
            new = new.next

    return new_head
