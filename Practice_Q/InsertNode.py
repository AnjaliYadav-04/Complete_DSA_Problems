class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_begin(head, data):
    new_node = Node(data)
    
    if head is not None:
        head.prev = new_node
        new_node.next = head
    
    head = new_node
    return head
