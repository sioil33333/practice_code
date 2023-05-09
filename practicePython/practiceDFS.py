

def dfs(node):
    visitNode.append(node)
    print(f'방문지점:{visitNode}')

    for cnt,i in enumerate(tree[node]):
        print(f'node: {i}')
        if i == 'E':
            print("STOP")
            exit()
        dfs(i)
        if(node == 'A'):
            continue
        print(f'node: {node}')

tree = {'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
visitNode = []

dfs('A')


#A : B C
#B : A D E
#C : A F G
#D : B
#E : B
#F : C
#G : C


