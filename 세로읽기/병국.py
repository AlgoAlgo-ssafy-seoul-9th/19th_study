arr = []
for i in range(4):
    arr.append(list(input()))
answer = ''
dir = 0
while True:
    aa =''
    flag = True
    for i in range(len(arr)):
        if len(arr[i]) == 0:
            flag = False
        else:
            flag = True
            break
    if flag == False:
        break
    if arr[dir%4]:
        aa = arr[dir%4].pop(0)
    dir += 1
    answer += aa
print(answer)