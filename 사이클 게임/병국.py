import sys
input = sys.stdin.readline
def find(a):
    while a != parent[a]:
        a = parent[a]
    return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n,m = map(int,input().split())
answer = 0
parent = [i for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())

    # 부모다르면 부모합쳐줘
    if parent[a] != parent[b]:
        union(a,b)

    # 부모가 같다? 사이클
    else:
        answer = i+1
# print(parent)
print(answer)