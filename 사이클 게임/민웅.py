# 20040_사이클게임_cycle-game
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adjL = [[] for _ in range(N)]
parent = [i for i in range(N)]

def findset(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(x, y):
    parent[findset(y)] = findset(x)


ans = 0
for _ in range(M):
    s, g = map(int, input().split())
    ans += 1
    if findset(s) == findset(g):
        break
    union(s, g)
else:
    ans = 0

print(ans)