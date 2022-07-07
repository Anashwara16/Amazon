
# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        
        l, h = 0, len(nums)-1

        while(l < h):
            
            mid = (l+h)//2

            if(nums[mid] < nums[mid+1]):
                l = mid + 1

            else:
                h = mid

        return l


if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    objectNums = Solution()
    print(objectNums.findPeakElement(nums))