
# 210. Course Schedule II

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adjacencyList = defaultdict(list)
        incomingEdges = {}
        coursePath = []

        for destination, source in prerequisites:
            adjacencyList[source].append(destination)
            incomingEdges[destination] = 1 + incomingEdges.get(destination, 0)

        print(adjacencyList)
        zeroIncoming = deque()

        for course in range(numCourses):
            if course not in incomingEdges:
                zeroIncoming.append(course)

        while zeroIncoming:

            currentCourse = zeroIncoming.pop()
            coursePath.append(currentCourse)

            for outgoingNode in adjacencyList[currentCourse]:
                incomingEdges[outgoingNode] -= 1

                if incomingEdges[outgoingNode] == 0:
                    zeroIncoming.append(outgoingNode)

        return coursePath


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    objectNums = Solution()
    print(objectNums.findOrder(numCourses, prerequisites))
