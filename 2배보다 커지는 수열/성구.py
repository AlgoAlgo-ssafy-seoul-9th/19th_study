# 2배보다 커지는 수열 
# 박영준 교수님의 힌트를 봤습니다
import sys
input = sys.stdin.readline

'''
0 1 2 3 4 5 6 7 8 9 10
0 1 0 0 0 0 0 0 0 0 0 
1 0 1 1 0 0 0 0 0 0 0
2 0 0 0 1 1 0 0 0 0 0
3 0 0 0 0 0 0 0 1 1 2
'''


def solution():
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for i in range(1, n+1)]
    for i in range(1, m//2**(n-1)+1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(2**(i), m//2**(n-i-1)+1):
            dp[i][j] += sum(dp[i-1][:j//2+1])

    print((sum(dp[n-1])) % 1_000_000_007)


if __name__ == "__main__":
    solution()