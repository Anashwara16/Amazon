
# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0
    
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
                
            tmp = curMax
            curMax = max(n*tmp, n*curMin, n)
            curMin = min(n*tmp, n*curMin, n)
            res = max(res, curMax)
            
        return res


if __name__ == "__main__":
    nums = [2,3,-2,4]
    objectNums = Solution()
    print(objectNums.maxProduct(nums))