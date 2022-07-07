class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)

        if not nums: 
            return 0

        robNextPlusOne = 0
        robNext = nums[n-1]
        current = 0

        for i in range(n-2, -1, -1):
            current = max(robNext, robNextPlusOne + nums[i]) 

            robNextPlusOne = robNext
            robNext = current

        return robNext

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    objectNums = Solution()
    print(objectNums.rob(nums))
