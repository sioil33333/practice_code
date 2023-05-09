from collections import deque

tree = {'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
visitNode = ['A']

bfs = deque()
print("node: A")
print(f"방문지점:{visitNode}")
bfs.append('A')

while bfs:
    q = bfs.popleft()

    for i in tree[q]:
        print(f"node: {i}")
        if i == 'E':
            print('STOP')
            exit()
        bfs.append(i)
        visitNode.append(i)
        print(f"방문지점:{visitNode}")