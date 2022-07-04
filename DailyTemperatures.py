
# 739. Daily Temperatures


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        answer = [0]*len(temperatures)
        temperatureStack = []

        for index, temperature in enumerate(temperatures):

            while temperatureStack and temperature > temperatureStack[-1][0]:
                stackTemperature, stackIndex = temperatureStack.pop()
                answer[stackIndex] = index - stackIndex

            temperatureStack.append([temperature, index])

        return answer


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    objectNums = Solution()
    print(objectNums.dailyTemperatures(temperatures))
