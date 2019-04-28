def has_cycle(head):
    tail_slow, tail_fast = head, head
    while (tail_slow and tail_fast and tail_fast.next):
        tail_slow = tail_slow.next
        tail_fast = tail_fast.next.next
        if tail_fast == tail_slow:
            return True
    return False
