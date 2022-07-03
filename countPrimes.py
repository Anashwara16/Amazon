
# 204. Count Primes

import math 

class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2: 
            return 0
        
        nums = [False, False] + [True]*(n-2)
        
        for p in range(2, int(math.sqrt(n))+1):
            
            if(nums[p]): 
                
                for multiple in range(p*p, n, p):
                    nums[multiple] = False  
    
        return sum(nums)


if __name__ == "__main__":
    n = 10
    objectNums = Solution()
    print(objectNums.countPrimes(n))