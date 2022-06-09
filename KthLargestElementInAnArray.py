
# 215. Kth Largest Element in an Array

from random import randint


class Solution:
    def findKthLargest(self, nums, k):

        def partition(left, right, pivotIndex):

            pivot = nums[pivotIndex]
            nums[right], nums[pivotIndex] = nums[pivotIndex], nums[right]

            storeIndex = left

            for i in range(left, right):

                if nums[i] <= pivot:
                    nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
                    storeIndex += 1

            nums[right], nums[storeIndex] = nums[storeIndex], nums[right]

            return storeIndex

        def quickselect(left, right, kSmallest):

            if left == right:
                return nums[left]

            pivotIndex = randint(left, right)
            pivotIndex = partition(left, right, pivotIndex)

            if kSmallest == pivotIndex:
                return nums[kSmallest]

            elif kSmallest < pivotIndex:
                return quickselect(left, pivotIndex-1, kSmallest)

            else:
                return quickselect(pivotIndex+1, right, kSmallest)

        return quickselect(0, len(nums)-1, len(nums)-k)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    objectNums = Solution()
    print(objectNums.findKthLargest(nums, k))
