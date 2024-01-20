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