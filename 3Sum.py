
# 15. 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i-1] != nums[i]:
                print("Send i:", i)
                self.twoSum(nums, i, result)

        return result
    
    def twoSum(self, nums: list[int], i: int, result: list[list[int]]):
        
        seen = set()
        j = i + 1 

        while j < len(nums):
            
            complement = -(nums[i]) - nums[j]
            print("i & j", nums[i], nums[j])
            print("Complement: ", complement)
            print("Set: ", seen)
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                while j+1 < len(nums) and nums[j] == nums[j+1]: 
                    j += 1

            seen.add(nums[j])
            j += 1       

        print(result)
        return result


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    objectNums = Solution()
    print(objectNums.threeSum(nums))