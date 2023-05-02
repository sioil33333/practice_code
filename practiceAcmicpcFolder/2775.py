#https://www.acmicpc.net/problem/2775

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        dp = [0]*10001
        k = int(input())
        n = int(input())
        cnt = n
        for i in range(1,n+1):
            dp[i] = i
        for i in range(k):
            cnt += 1
            dp[cnt]= 1
            for j in range(1,n):
                cnt += 1
                dp[cnt]= dp[cnt-1] + dp[cnt-n]
        print(dp[cnt])
