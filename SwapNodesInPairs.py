
# 24. Swap Nodes in Pairs


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        previous, current = dummy, head

        while current and current.next:

            # Save pointers
            nextPair = current.next.next
            second = current.next

            # Reverse nodes
            second.next = current
            current.next = nextPair

            # Update dummy node
            previous.next = second

            # Update pointers
            previous = current
            current = nextPair

        return dummy.next
