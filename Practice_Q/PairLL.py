def find_pairs(head, target):
    left = head
    right = head

    # move right to last
    while right.next:
        right = right.next

    result = []

    while left != right and right.next != left:
        s = left.data + right.data
        
        if s == target:
            result.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif s < target:
            left = left.next
        else:
            right = right.prev

    return result
