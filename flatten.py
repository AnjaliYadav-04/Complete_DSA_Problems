def flatten(head):
    curr = head

    while curr:
        if curr.child:
            nxt = curr.next
            child = flatten(curr.child)

            curr.next = child
            child.prev = curr
            curr.child = None

            temp = child
            while temp.next:
                temp = temp.next

            temp.next = nxt
            if nxt:
                nxt.prev = temp

        curr = curr.next

    return head
