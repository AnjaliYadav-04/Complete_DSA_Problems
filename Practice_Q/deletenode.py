def delete_node(head, key):
    temp = head

    while temp:
        if temp.data == key:

            if temp.prev:
                temp.prev.next = temp.next
            else:
                head = temp.next

            if temp.next:
                temp.next.prev = temp.prev

            break

        temp = temp.next

    return head
