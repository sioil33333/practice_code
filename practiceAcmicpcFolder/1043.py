#https://www.acmicpc.net/problem/1043
import sys; input = sys.stdin.readline

if __name__ == '__main__':
    n,m = map(int,input().split())
    truthPeoples = set(input().split()[1:])
    parties = []
    
    for _ in range(m):
        party = set(input().split()[1:])
        if party & truthPeoples:
            truthPeoples = truthPeoples.union(party)
            m -= 1
            continue
        parties.append(party)
    
    for _ in range(m):
        for party in parties:
            if party & truthPeoples:
                truthPeoples = truthPeoples.union(party)
    
    for party in parties:
        if party & truthPeoples:
            m -= 1
    print(m)