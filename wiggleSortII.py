
# 324. Wiggle Sort II

import numpy
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return None
        
        def A(i):
            return (2*i+1) % (n|1)

        midIndex = int(n/2)
        key = numpy.median(nums)

        i,j,k=0,0,n-1

        while j <= k:
            if nums[A(j)] > key:
                nums[A(j)],nums[A(i)]=nums[A(i)],nums[A(j)]
                i,j = i+1,j+1
            elif nums[A(j)] < key:
                nums[A(j)],nums[A(k)]=nums[A(k)],nums[A(j)]
                k -= 1
            else:
                j += 1
        
        print(nums)


if __name__ == "__main__":
    nums = [1,5,1,1,6,4]
    objectNums = Solution()
    print(objectNums.wiggleSort(nums))