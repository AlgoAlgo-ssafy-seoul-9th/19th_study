# 19th_study

### 19주차 알고리즘스터디

# 지난주 문제

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [사다리 조작](https://www.acmicpc.net/problem/15684)

### [민웅](<./사다리 조작/민웅.py>)

```py
# 15684_사다리조작_Ladder-control
# 지금 시간초과
import sys
input = sys.stdin.readline

def ladder_check(L, n):
    h = 0
    n_check = n
    while True:
        if h == H:
            break
        now = L[h][n_check]

        if now == 0:
            h += 1
        else:
            if L[h][n_check] == 'l':
                n_check += 1
            else:
                n_check -= 1
            h += 1

    if n_check == n:
        return True
    else:
        return False


def bt(l_lst, l_idx, ladder_now, picked):
    global ans
    global l_cnt

    if picked > 3:
        return

    if ans != -1:
        return

    for i in range(N):
        tmp = ladder_check(ladder_now, i)
        if not tmp:
            break
    else:
        ans = picked
        return

    while True:
        x, y = l_lst[l_idx]
        if ladder_now[x][y] == 0 and ladder_now[x][y+1] == 0:
            break

        if l_idx < l_cnt-1:
            l_idx += 1
        else:
            break
    if l_idx != l_cnt-1:
        bt(l_lst, l_idx+1, ladder_now, picked)

    x, y = l_lst[l_idx]
    ladder_now[x][y] = 'l'
    ladder_now[x][y+1] = 'r'
    bt(l_lst, l_idx, ladder_now, picked+1)
    ladder_now[x][y] = 0
    ladder_now[x][y+1] = 0



N, M, H = map(int, input().split())

ladder = [[0]*N for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 'l'
    ladder[a-1][b] = 'r'

l_sub = []
l_cnt = 0
for i in range(H):
    for j in range(N-1):
        if ladder[i][j] == 0 and ladder[i][j+1] == 0:
            l_sub.append([i, j])
            l_cnt += 1

ans = -1
if l_sub:
    bt(l_sub, 0, ladder, 0)
print(ans)
```

### [상미](<./사다리 조작/상미.py>)

```py

```

### [병국](<./사다리 조작/병국.py>)

```py
def check():
    for i in range(N):
        now = i
        for j in range(H):
            if ladder[j][now] == 1:
                now += 1
            elif now >= 1 and ladder[j][now-1] == 1:
                now -= 1
        # 하나라도 시작이랑 도착 다르면 바로 리턴
        if now != i:
            return False
    return True

def back(cnt, x, y):
    global answer
    if check(): # True면 된다는거
        answer = min(cnt,answer)
        return
    elif cnt == 3 or answer <= cnt:
        return

    # 가로선 탐색해보자,
    for i in range(x, H):
        # 아직 x행 보고 있으면
        if i == x:
            # 가로선 고정
            tmp = y
        else:
            tmp = 0
        # 세로선
        for j in range(tmp, N-1):
            # 내위치, 오른쪽위치에 사다리없으면
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                # 근데 왼쪽에있다면..? 일직선되니까 패스
                if j > 0 and ladder[i][j-1] == 1:
                    continue
                ladder[i][j] = 1
                # 행은 같은데 열은 두칸뒤로 가야된다, 일직선 되면 안되니까.
                back(cnt+1,i,j+2)
                ladder[i][j] = 0


N, M, H = map(int,input().split())
ladder = [[0]*(N) for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    ladder[a-1][b-1] = 1
# print(ladder)

answer = 4
back(0, 0, 0)
if answer < 4:
    print(answer)
else:
    print(-1)
```

### [성구](<./사다리 조작/성구.py>)

```py
# 15684 사다리 조작
import sys
input = sys.stdin.readline


def check_ladder() -> bool:
    for i in range(N):
        y, x = 0, i
        while y < H:
            if ladders[y][x] == 1:      # 1이면 왼쪽으로 이동
                x -= 1
            elif ladders[y][x] == 2:    # 2면 오른쪽으로 이동
                x += 1
            y += 1
        if x != i:      # i -> i 가 아닐경우 False
            return 0
    return 1        # 모두 i -> i 되면 True

# 백트래킹
def bt(cnt:int, start_i:int) -> None:
    global ans

    if check_ladder():  # i-> i 체크
        # 된다면 cnt 저장
        ans = min(cnt, ans)
        return
    if cnt == 3:        # 3 이하일 때만 허용
        return
    if cnt >= ans:
        return
    # i -> i가 안 될 경우, 탐색 중이었던 높이부터 체크하면 됨
    for i in range(start_i, H):
        for j in range(N-1):
            if not ladders[i][j] and not ladders[i][j+1]:
                ladders[i][j] = 2
                ladders[i][j+1] = 1
                bt(cnt+1, i)
                ladders[i][j] = 0
                ladders[i][j+1] = 0
    return


if __name__ == "__main__":
    N, M, H = map(int, input().split())
    ladders = [[0] * N for _ in range(H)]
    visited = [[0] * N for _ in range(H)]
    for _ in range(M):
        # 1 -> 왼쪽, 2 -> 오른쪽
        a, b = map(int, input().split())
        ladders[a-1][b-1] = 2
        ladders[a-1][b] = 1
    ans = 5
    bt(0,0)
    print(-1 if ans > 3 else ans)

```

<br/><br/>

</div>

</details>

</br></br></br>

# 이번주 문제

<details open>
<summary>접기/펼치기</summary>
<div markdown="1">

## [택배 배송](https://www.acmicpc.net/problem/5972)

### [민웅](<./택배 배송/민웅.py>)

```py

```

### [상미](<./택배 배송/상미.py>)

```py

```

### [병국](<./택배 배송/병국.py>)

```py

```

### [성구](<./택배 배송/성구.py>)

```py

```

### [승우](<./택배 배송/승우.py>)

```py

```

</div>
</details>
<br><br>

# 알고리즘 설명

<details>
<summary>접기/펼치기</summary>

</details>
