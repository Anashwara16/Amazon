# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6

    startIndex, endIndex, nextIndex = 0, 0, 0
    maxSum = totalSum = 0

    for i in range(len(A)):

        if A[i] < 0:
            nextIndex = i + 1
            maxSum = 0

        else:
            maxSum += A[i]

        if maxSum > totalSum:
            totalSum = maxSum
            startIndex = nextIndex
            endIndex = i

    return totalSum
