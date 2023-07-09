#https://www.acmicpc.net/problem/1753





if __name__ == '__main__':
    inf = 10e9

    v,e = map(int,input().split()) #정점, 간선
    graph = {} #그래프 dict
    for i in range(1,v+1):
        graph[i] = {}
    k = int(input()) #start

    for _ in range(e):
        u, d, w = map(int,input().split())
        graph[u][d] = w #정점 u에 비용이 w인 간선 d 저장
