# 19th_study

### 19주차 알고리즘스터디

# 지난주 문제

<details>
<summary>접기/펼치기</summary>
<div markdown="1">


## [세로 읽기](https://www.codetree.ai/problems/vertical-reading/description)


### [민웅](<./세로읽기/민웅.py>)

```py
import sys
# input = sys.stdin.readline

word_lst = []
max_l = 0

for _ in range(4):
    tmp = list(input())
    if len(tmp) > max_l:
        max_l = len(tmp)
    word_lst.append(tmp)

# print(word_lst)
# print(max_l)

new_lst = [[-1]*max_l for _ in range(4)]
for i in range(4):
    for j in range(len(word_lst[i])):
        new_lst[i][j] = word_lst[i][j]

ans = ''

for i in range(max_l):
    for j in range(4):
        if new_lst[j][i] != -1:
            ans += str(new_lst[j][i])
print(ans)
```

### [상미](<./세로읽기/상미.py>)

```py

```

### [병국](<./세로읽기/병국.py>)

```py

```

### [성구](<./세로읽기/성구.py>)

```py

```

### [승우](<./세로읽기/승우.py>)

```py

```

## [2배보다 커지는 수열](https://www.codetree.ai/training-field/search/problems/a-sequence-greater-than-twice/description?page=14&pageSize=20)


### [민웅](<./2배보다 커지는 수열/민웅.py>)

```py

```

### [상미](<./2배보다 커지는 수열/상미.py>)

```py

```

### [병국](<./2배보다 커지는 수열/병국.py>)

```py

```

### [성구](<./2배보다 커지는 수열/성구.py>)

```py

```

### [승우](<./2배보다 커지는 수열/승우.py>)

```py

```

## [코드트리 사내 메신저](https://www.codetree.ai/problems/codetree-internal-messenger/description)


### [민웅](<./코드트리 사내 메신저/민웅.py>)

```py
#3번 코드트리메신저
import sys
input = sys.stdin.readline

N = int(input())

def c_tree(n):
    if adjL[n]:
        child_lst = []
        for child in adjL[n]:
            c_time = c_tree(child)
            child_lst.append(c_time)
        child_lst.sort(reverse=True)

        max_child = 0
        for i in range(len(child_lst)):
            max_child = max((child_lst[i]+1)+i, max_child)
        return max_child
    else:
        return 0


employee_lst = list(map(int, input().split()))
adjL = [[] for _ in range(N + 1)]

for i in range(1, N):
    adjL[employee_lst[i]].append(i + 1)

print(c_tree(1))
```

### [상미](<./코드트리 사내 메신저/상미.py>)

```py

```

### [병국](<./코드트리 사내 메신저/병국.py>)

```py

```

### [성구](<./코드트리 사내 메신저/성구.py>)

```py

```

### [승우](<./코드트리 사내 메신저/승우.py>)

```py

```

<br/><br/>

</div>

</details>

</br></br>

# 이번주 문제

<details open>
<summary>접기/펼치기</summary>
<div markdown="1">

## [사이클 게임](https://www.acmicpc.net/problem/20040)

### [민웅](<./사이클 게임/민웅.py>)

```py
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
```

### [상미](<./사이클 게임/상미.py>)

```py

```

### [병국](<./사이클 게임/병국.py>)

```py

```

### [성구](<./사이클 게임/성구.py>)

```py

```

### [승우](<./사이클 게임/승우.py>)

```py

```

</div>
</details>
<br><br>

# 알고리즘 설명

<details>
<summary>접기/펼치기</summary>

</details>
