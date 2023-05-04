#https://www.acmicpc.net/problem/2263
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

#function
# 첫 번째 시도
# def findpreorder(inorder:list, postorder:list) -> None:
    
#     tempLenInoder = len(inorder)
#     root = postorder[-1]
    
#     print(root, end=" ")
#     if tempLenInoder == 1:
#         return
    
#     #2개의 각각의 inorder, postorder로 쪼개기
#     for i in range(tempLenInoder):
#         if inorder[i] == root:
#             leftInoder = inorder[0:i]
#             rightInoder = inorder[i+1:tempLenInoder]
#             break
    
#     if not leftInoder:
#         findpreorder(rightInoder, postorder[0:tempLenInoder-1])
#     elif not rightInoder:
#         findpreorder(leftInoder, postorder[0:tempLenInoder-1])
#     else:
#         temp = 0
#         for i in range(1, tempLenInoder-1):
#             if postorder[i] not in leftInoder:
#                 temp = i
#                 break
#         findpreorder(leftInoder, postorder[0:temp])
#         findpreorder(rightInoder, postorder[temp:tempLenInoder-1])
#     return


def findingPreorder(ins:int, inf:int, posts:int, postf:int)->None:
    if ins > inf or posts > postf:
        return
    
    root = postorder[postf]

    leftIn = nums[root] - ins
    rightIn = inf - nums[root]

    print(root, end=' ')
    findingPreorder(ins,ins+leftIn-1,posts,posts+leftIn-1)
    findingPreorder(inf-rightIn+1,inf,postf-rightIn,postf-1)

#main
if __name__ == '__main__':
    n = int(input())
    inorder = list(map(int,input().split()))
    postorder = list(map(int,input().split()))

    nums = [0]*(n+1)
    for i in range(n): nums[inorder[i]] = i
    findingPreorder(0,n-1,0,n-1)