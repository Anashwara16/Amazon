
# 543. Diameter of Binary Tree


class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        longestDiameter = 0

        def longestPath(currentRoot):

            nonlocal longestDiameter

            if not currentRoot:
                return 0

            leftSubtree = longestPath(currentRoot.left)
            rightSubtree = longestPath(currentRoot.right)

            longestDiameter = max(
                longestDiameter, (leftSubtree + rightSubtree))

            return max(leftSubtree, rightSubtree) + 1

        longestDiameter(root)

        return longestDiameter


if __name__ == "__main__":
    root = [1, 2, 3, 4, 5]
    objectNums = Solution()
    print(objectNums.diameterOfBinaryTree(root))
