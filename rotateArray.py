
# 189. Rotate Array

from tkinter import N


class Solution:

    def reverse(self, nums: list[int], start: int, end: int):
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: list[int], k : int) -> list[int]:

        n = len(nums)-1
        k %= n 
        
        self.reverse(nums, 0, n)

        self.reverse(nums, 0, k-1)

        self.reverse(nums, k, n)

        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    objectNums = Solution()
    print(objectNums.rotate(nums, k))