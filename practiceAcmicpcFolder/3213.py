#지뢰찾기
#https://www.acmicpc.net/problem/1996

case = []
n = int(input())
for i in range(n):
    case.append(input())

for y in range(n):
    for x in range(n):
        if case[y][x] != '.':
            print("*",end='')
            continue
        cnt = 0
        for dy in range(max(0,y-1),min(n,y+2)):
            for dx in range(max(0,x-1),min(n,x+2)):
                if case[dy][dx] != '.':
                    cnt += int(case[dy][dx])
        if cnt >= 10:
            print("M",end='')
        else:
            print(cnt,end='')
    print()
                