#https://www.acmicpc.net/problem/1167
import sys; input = sys.stdin.readline

def dfs(num:int)->None:
    global maxlength
    check = True

    for node in graph[num]:
        
        # if node[0] in currents:
        #     continue
        currentDfs.append(node[0])
        dfs(node[0])
        currentDfs.pop()
        check = False

    if check:
        print(currentDfs)
        length = 0
        for i in currentDfs:
            length += i[1]
        maxlength = max(length,maxlength)
if __name__ == '__main__':
    #graph[tempNum][i][0] == 간선 i, graph[tempNum][i][1] == 정점과 간선 간의 거리  
    graph = {}
    
    v = int(input())
    
    for i in range(v):
        temp = tuple(map(int,input().split()))
        tempNum = temp[0]
        graph[tempNum] = []
        for i in range(1, len(temp)-1, 2):
            graph[tempNum].append([temp[i],temp[i+1]])
    
    currentDfs = []
    maxlength = 0
    for i in range(1,v):
        currentDfs.append([i,0])
        dfs(i)
        currentDfs.pop()
    
    print(maxlength)