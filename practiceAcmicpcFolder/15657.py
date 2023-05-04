#https://www.acmicpc.net/problem/15657


def dfs(cnt:int)->None:
    global stack
    if len(stack) == m:
        print(*stack)
        return
    
    for i in range(cnt,n):
        stack.append(case[i])
        dfs(i)
        stack.pop()
    
if __name__ == '__main__':
    stack = []
    n,m = map(int,input().split())
    case = sorted(list(map(int,input().split())))

    dfs(0)