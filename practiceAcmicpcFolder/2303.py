#숫자 게임
#https://www.acmicpc.net/problem/2303

a = int(input())
maxs = 0
result = ""
for nums in range(a):
    case = tuple(map(int,input().split()))
    max = 0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                cur = int(str(case[i] + case[j] + case[k])[-1])
                if cur > max:
                    max = cur
    if max >= maxs:
        maxs = max
        result = nums + 1
print(result)
