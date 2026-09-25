class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class Solution:

    def mergeList(self, lists: list[ListNode | None])-> ListNode |None:
        values=[]

        for head in lists:
            current=head

            while current:
                values.append(current.val)
                current=current.next

        values.sort()   

        dummy=ListNode(0)
        current=dummy

        for value in values:
            current.next=ListNode(value)
            current=current.next

        return dummy.next     


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)



lists = [list1, list2, list3]



solution = Solution()
result = solution.mergeList(lists)


#result
while result:
    print(result.val, end=" -> ")
    result = result.next

print("None")    
