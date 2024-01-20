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