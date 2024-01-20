def find_set(n):
    c = n
    while rep[c] != c:
        c = rep[c]
    return c

def union(a, b):
    rep[find_set(b)] = find_set(a)

n, m = map(int, input().split())
rep = [ i for i in range(n+1)]

edge = [list(map(int, input().split())) for _ in range(m)]
ans = 0                 # 사이클이 생기지 않은채 끝나면 0
for i in range(m):
    a = find_set(edge[i][0])
    b = find_set(edge[i][1])
    if a==b:            # 사이클이 생기면 중단
       ans = i+1
       break
    union(a, b)

print(ans)
