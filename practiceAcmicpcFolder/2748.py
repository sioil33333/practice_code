#https://www.acmicpc.net/problem/2748

dp = [0]*10001

if __name__ == '__main__':
    n = int(input())
    if n <= 2:
        print(1)
        exit()
    
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
