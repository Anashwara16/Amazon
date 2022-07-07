
# 143. Reorder List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        current = slow

        while current:
            followingCurrent = current.next
            current.next = previous
            previous = current
            current = followingCurrent

        first = head
        second = previous

        while second.next:
            followingFirst, followingSecond = first.next, second.next
            first.next = second
            second.next = followingFirst
            first, second = followingFirst, followingSecond

        return head
