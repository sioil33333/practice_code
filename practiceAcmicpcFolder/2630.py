#https://www.acmicpc.net/problem/2630


import sys; input = sys.stdin.readline

#method line

def check(cury:int, curx:int, n:int) ->tuple:
    if n == 0:
        return
    for y in range(2):
        for x in range(2):
            dy,dx = cury+y*n,curx+x*n
            color = case[dy][dx]
            checks = True
            for i in range(n):
                for j in range(n):
                    if color != case[dy+i][dx+j]:
                        checks = False
                        check(dy,dx,n//2)
                        break
                if checks == False:
                    break
            if checks:
                if color == 0:
                    global white
                    white += 1
                else:
                    global black 
                    black += 1

def allcheck(n:int):
    #모든 칸이 같은 색인지 확인. 맞으면 프린트 후 프로그램 종료

    t = case[0][0]
    for i in range(n):
        for j in case[i]:
            if j != t:
                return 0
    if t == 0:
        print(f'{1}\n{0}')
    else:
        print(f'{0}\n{1}')
    exit()


#main

n = int(input())
case = []

for i in range(n):
    case.append(list(map(int,input().split())))

allcheck(n)

white, black = 0, 0
check(0,0,n//2)

print(f'{white}\n{black}')