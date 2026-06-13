def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    temp = head

    while temp.next:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp

    return head
