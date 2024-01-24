import sys
input = sys.stdin.readline


def solution(arr:list) -> str:
    ans = ""
    for j in range(max(map(lambda x:len(x), arr))):
        for i in range(4):
            if j >= len(arr[i]):
                continue
            ans += arr[i][j]
    return ans

if __name__ == "__main__":
    arr = [input().strip() for _ in range(4)]
    print(solution(arr))