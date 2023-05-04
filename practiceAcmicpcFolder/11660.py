#https://www.acmicpc.net/problem/11660
import sys; input = sys.stdin.readline
#function
def calculation(x1:int,y1:int,x2:int,y2:int)->int:
    return dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]

#main
case = []
if __name__ == '__main__':
    n,m = map(int,input().split())
    for i in range(n):
        case.append(list(map(int,input().split())))
    dp = [[0]*(n+1) for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + case[i-1][j-1]


    for _ in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        print(calculation(x1,y1,x2,y2))