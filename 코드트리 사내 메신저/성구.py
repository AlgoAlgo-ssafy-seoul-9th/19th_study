# 사내 메신저
import sys
input = sys.stdin.readline    


def inorder(person:int, call:list):
    # 내가 연락해야할 리스트(비용)
    contact = []
    for next in call[person]:
        # 내가 연락할 사람이 앞으로 연락할 때 걸리는 시간 저장
        contact.append(1+inorder(next, call)) # 1은 본인에게 inorder은 아랫사람에게
    if contact: # 만약 다른사람에게 연락을 해야한다면
        contact.sort(reverse=1)     # 연락할 사람이 많은 사람부터 연락 시작
        for i in range(len(contact)):   # 순서 비용 추가
            contact[i] += i

        return max(contact) # 가장 비싼 비용이 모두 연락하는 비용과 같음
    return 0
        


def solution():
    N = int(input())
    people = list(map(int, input().split()))
    call = [[] for _ in range(N+1)]
    # 연락 트리 만들기
    for i in range(1, N):
        call[people[i]].append(i+1)
    ans = inorder(1, call)
    print(ans)
    

if __name__ == "__main__":
    solution()