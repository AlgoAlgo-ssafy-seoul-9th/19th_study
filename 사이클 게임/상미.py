## 20040_백준_사이클 게임
import sys
input = sys.stdin.readline

# 루트노드 찾기
def findset(node):
    while parent[node] != node:
        node = parent[node]
    return node

# 루트노드 갱신
def union(x, y):
    parent[findset(y)] = findset(x)     # y의 루트노드를 x의 루트노드로 갱신

n, m = map(int, input().split())

# 각 정점에 대한 부모 초기화
parent = [i for i in range(n)]
cnt = 1
for i in range(m):
    s, e = map(int, input().split())
    if s > e:           # 작은 번호, 큰 번호 순으로 정렬 통일
        s, e = e, s
    if findset(s) != findset(e):    # 루트노드가 다르면 이을 수 있다
        cnt += 1        # 추가된 간선 수
        union(s, e)     # 이어졌으니까 루트노드 갱신해주고
    else:               # 이미 루트노드 같은 경우엔 둘이 이으면 사이클 생기니까
        break
if cnt == m+1:      # 만약 주어진 모든 선 돌았으면 사이클 안 생겼다는 뜻
    cnt = 0
print(cnt)

