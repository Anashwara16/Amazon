# 102. Binary Tree Level Order Traversal

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:

        if not root:
            return []

        q = collections.deque()
        q.append(root)
        result = []

        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                result.append(level)

        return result


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    objectNums = Solution()
    print(objectNums.levelOrder(root))
