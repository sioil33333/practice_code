#https://www.acmicpc.net/problem/2407

if __name__ == '__main__':
    n,m = map(int,input().split())
    
    op = 1
    operand = 1
    for i in range(1,min(m,n-m)+1):
        op *= (n-i+1)
        operand *= i
    print(op//operand)