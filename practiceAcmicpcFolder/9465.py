#https://www.acmicpc.net/problem/9465

import sys; input = sys.stdin.readline

#function

#main
if __name__ == "__main__":
    #테스트 케이스 갯수
    t = int(input())

    for _ in range(t):
        case = []
        n = int(input())

        for i in range(2):
            case.append(list(map(int,input().split())))
        if n != 1:
            case[0][1] += case[1][0]
            case[1][1] += case[0][0]
            for i in range(2,n):
                case[0][i] += max(case[1][i-2],case[1][i-1])
                case[1][i] += max(case[0][i-2],case[0][i-1])
        print(max(case[0][n-1],case[1][n-1]))
        
