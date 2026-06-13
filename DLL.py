def delete_all(head, key):
    curr = head

    while curr:
        if curr.data == key:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = curr.next

            if curr.next:
                curr.next.prev = curr.prev

        curr = curr.next

    return head
