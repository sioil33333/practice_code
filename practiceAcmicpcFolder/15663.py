#https://www.acmicpc.net/problem/15663

resultStack = []
def dfs()->None:
    global stack
    if len(stack) == m:
        stacks = [case[i] for i in stack]
        if stacks in resultStack:
            return
        print(*stacks)
        resultStack.append(stacks)
        return
    
    for i in range(0,n):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()
    
if __name__ == '__main__':
    stack = []
    n,m = map(int,input().split())
    case = sorted(list(map(int,input().split())))

    dfs()