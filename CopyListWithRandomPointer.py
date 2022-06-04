
# 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        ogToCopy = {None: None}

        cur = head
        while cur:
            newNode = Node(cur.val)
            ogToCopy[cur] = newNode
            cur = cur.next

        cur = head
        while cur:
            newNode = ogToCopy[cur]
            newNode.next = ogToCopy[cur.next]
            newNode.random = ogToCopy[cur.random]
            cur = cur.next

        return ogToCopy[head]
