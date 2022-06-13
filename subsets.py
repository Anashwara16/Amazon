
# 78. Subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subset = []
        result = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            print("Iteration: ", i)    
            print("Before append -- ", subset)      
            subset.append(nums[i])
            print("After append -- ", subset)    
            dfs(i+1)    
               
            print("Iteration before pop: ", i)    
            print("Before pop -- ", subset)         
            subset.pop()
            print("After pop -- ", subset)  
            print("Iteration after pop: ", i)   
            dfs(i+1)
            print("Iteration i+1 after pop: ", i)   
        
        dfs(0)
        return result


if __name__ == "__main__":
    nums = [1,2,3]
    objectNums = Solution()
    print(objectNums.subsets(nums))