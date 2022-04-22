import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(n):
    stair = [0]
    for _ in range(n):
        stair.append(int(input()))
    if n < 3:
        return sum(stair[:n])

    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = stair[1], stair[1] + stair[2]

    for index in range(3, n + 1):
        dp[index] = max(dp[index - 3] + stair[index - 1], dp[index - 2]) + stair[index]

    return dp[n]

print(solution(int(input())))