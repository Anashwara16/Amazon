# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, C):
    # write your code in Python 3.6
    n = len(S)
    minCost = 0
    i = 0

    while (i+1) < n:

        if S[i] == S[i+1]:
            minCost += min(C[i], C[i+1])

        i += 1

    return minCost
