
# 378. Kth Smallest Element in a Sorted Matrix

from bisect import bisect_right

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        
        l, h, n = matrix[0][0], matrix[-1][-1], len(matrix)

        def lessThanK(mid):
            count = 0

            print("*** NEW ITERATION ***") 
            for r in range(n): 
                x = bisect_right(matrix[r], mid)
                print("Iteration: ", r)
                print("X value: ", x)
                count += x
                print("Count: ", count)
            
            return count

        while(l < h):
            
            mid = (l+h)//2
            print("MID: ", mid)

            if(lessThanK(mid) < k):
                l = mid+1

            else:
                h = mid     

        return l


if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    objectNums = Solution()
    print(objectNums.kthSmallest(matrix, k))