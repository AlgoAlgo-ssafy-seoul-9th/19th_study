import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

def findset(n):
    while parent[n] != n:
        n = parent[n]
    return n

def union(a, b):
    parent[findset(b)] = findset(a)


parent = [i for i in range(n)]
edge = [map(int,input().split()) for _ in range(m)]

answer = 0

for i in range(m):
    a, b = edge[i]
    if findset(a) == findset(b):
        answer = i + 1
        break
    union(a, b)

print(answer)
