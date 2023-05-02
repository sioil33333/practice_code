#https://www.acmicpc.net/problem/1010

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        if n == m:
            print(1)
            continue
        