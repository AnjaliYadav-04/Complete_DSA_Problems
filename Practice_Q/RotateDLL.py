def rotate(head, k):
    if not head:
        return head

    curr = head
    count = 1

    while count < k and curr:
        curr = curr.next
        count += 1

    if not curr:
        return head

    kth = curr

    while curr.next:
        curr = curr.next

    curr.next = head
    head.prev = curr

    head = kth.next
    head.prev = None
    kth.next = None

    return head
