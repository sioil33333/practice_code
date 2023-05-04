#https://www.acmicpc.net/problem/15654

def dfs():
    global stack
    if len(stack) == m:
        print(*stack)
        return
    
    for i in range(0,n):
        if case[i] not in stack:
            stack.append(case[i])
            dfs()
            stack.pop()
    
if __name__ == '__main__':
    stack = []
    n,m = map(int,input().split())
    case = sorted(list(map(int,input().split())))

    dfs()