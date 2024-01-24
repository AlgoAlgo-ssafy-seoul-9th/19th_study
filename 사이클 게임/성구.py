# 20040 사이클 게임
'''
- 반복문 find
    50548KB 552ms
- recursion find
    77844KB 700ms
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x:int):
    # recursion find
    # if x == spots[x]:
    #     return spots[x]
    # spots[x] = find(spots[x])

    # 반복문 find 
    tmp = x
    while tmp != spots[tmp]:
        tmp = spots[tmp]
    spots[x] = spots[tmp]
    return spots[x]


def union(num1:int, num2:int):
    f1 = find(num1)
    f2 = find(num2)
    # 같으면 Circle
    # 이미 이어져 있는 간선은 같은 root를 가짐
    if f1 != f2:
        spots[f2] = f1
        return 0
    return 1



def solution(N:int, M:int) -> int:
    # 2개 간선은 Circle이 될 수 없음
    for _ in range(2):
        s, e = map(int, input().split())
        union(s, e)
    # 3개부터 Circle 체크
    for turn in range(3, M+1):
        s, e = map(int, input().split())
        # Circle이 되면 1 반환
        if union(s, e):
            return turn
    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    spots = [i for i in range(N)] 
    print(solution(N, M))