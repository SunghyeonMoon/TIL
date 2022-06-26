import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline 


N, M = map(int, input().split())
row = set()
column = set()

for x in range(N):
    layer = input()
    for y in range(M):
        if layer[y] == 'X':
            row.add(x)
            column.add(y)
print(max(N - len(row), M - len(column)))