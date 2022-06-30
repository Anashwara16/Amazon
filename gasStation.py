class Solution:
    def canCompleteCircuit(self, gas, cost):
       
        n = len(gas)
        start = 0
        total_tank = current_tank = 0

        for i in range(n):

            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start = i + 1 
                current_tank = 0   

        return start if total_tank >= 0 else -1


if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    objectNums = Solution()
    print(objectNums.canCompleteCircuit(gas, cost))