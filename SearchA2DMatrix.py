# 74. Search a 2D Matrix


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows, cols = len(matrix)-1, len(matrix[0])-1

        top, bottom = 0, rows
        left, right = 0, cols

        while top <= bottom:

            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1

            elif target < matrix[mid][0]:
                bottom = mid - 1

            else:
                break

        if not (top <= bottom):
            return False

        while left <= right:

            pivot = (left + right)//2

            if matrix[mid][pivot] > target:
                right = pivot - 1

            elif matrix[mid][pivot] < target:
                left = pivot + 1

            else:
                return True

        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    objectNums = Solution()
    print(objectNums.searchMatrix(matrix, target))
