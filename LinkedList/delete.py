#2095. Delete the Middle Node of a Linked List

from typing import Optional

# Create ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If only one node exists
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head


# Helper function to print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Create linked list manually
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)

# Run solution
sol = Solution()
new_head = sol.deleteMiddle(head)

# Print result
printList(new_head)