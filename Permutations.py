
# 46. Permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result = []

        if(len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)): 

            n = nums.pop(0)
            print("Popped: ", n)
            
            perms = self.permute(nums)
            print("Perms: ", perms)

            for perm in perms: 
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result


if __name__ == "__main__":
    nums = [1,2,3]
    objectNums = Solution()
    print(objectNums.permute(nums))