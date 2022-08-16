

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode(0, head)
        left = dummy
        right = head

      # Advances first pointer so that the gap between first and second is n nodes apart

        while n and right:
            right = right.next
            n -= 1

      # Move first to the end, maintaining the gap

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    n = 2
    node = Solution()
    print(node.removeNthFromEnd(head, n))
