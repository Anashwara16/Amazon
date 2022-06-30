
# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        clone = {}

        def dfs(node):

            if node in clone:
                return clone[node]

            copyNode = Node(node.val)
            clone[node] = copyNode

            for neighbor in node.neighbors:
                copyNode.neighbors.append(dfs(neighbor))

            return copyNode

        return dfs(node) if node else None


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    objectNums = Solution()
    print(objectNums.cloneGraph(adjList))
