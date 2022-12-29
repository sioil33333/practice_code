#지뢰찾기
#https://www.acmicpc.net/problem/4108
while 1:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    case = []
    for i in range(a):
        case.append(input())
    for i in range(a):
        for j in range(b):
            if case[i][j] == ".":
                cnt = 0
                for y in range(max(i-1, 0), min(i+2, a)):
                    for x in range(max(j-1,0), min(j+2, b)):
                        if case[y][x] == '*':
                            cnt += 1
                print(cnt, end="")
            elif case[i][j] == "*":
                print("*", end="")
        print()