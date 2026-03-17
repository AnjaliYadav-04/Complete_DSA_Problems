def count_nodes(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def dll_to_bst(n):
    global head
    
    if n <= 0:
        return None

    left = dll_to_bst(n//2)

    root = Node(head.data)
    root.left = left

    head = head.next

    root.right = dll_to_bst(n - n//2 - 1)

    return root
