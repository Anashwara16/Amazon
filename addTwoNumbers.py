# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections
import llist

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        root = n = ListNode(0)

        while l1 or l2 or carry: 
            v1 = v2 = 0

            if l1: 
                v1 = l1.val
                l1 = l1.next
            else: 
                v1 = 0

            if l2: 
                v2 = l2.val
                l2 = l2.next
            else: 
                v2 = 0               

            carry, val = divmod(v1+v2+carry, 10)

            n.next = ListNode(val)
            n = n.next

        return root.next

if __name__ == "__main__":
    l1 = [2,4,3] 
    l2 = [5,6,4]
    objectNums = Solution()
    head = None
    head = objectNums.addTwoNumbers(l1,l2)
