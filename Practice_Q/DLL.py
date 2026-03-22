class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.random = None

def clone(head):
    curr = head

    while curr:
        new = Node(curr.data)
        new.next = curr.next
        curr.next = new
        curr = new.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    new_head = head.next

    while curr:
        copy = curr.next
        curr.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        curr = curr.next

    return new_head
