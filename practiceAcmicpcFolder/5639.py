#https://www.acmicpc.net/problem/5639
import sys; sys.setrecursionlimit(10**9)

#class
class node:
    def __init__(self, element:int) -> None:
        self.element = element
        self.rightnode = None
        self.leftnode = None


#function
def addTree(element:int)->None:
    #root
    global root
    currentNode = root
    while 1:
        if element < currentNode.element:
            if currentNode.leftnode == None:
                currentNode.leftnode = node(element)
                break
            currentNode = currentNode.leftnode
        elif currentNode.element < element:
            if currentNode.rightnode == None:
                currentNode.rightnode = node(element)
                break
            currentNode = currentNode.rightnode
    return

def printTree(node:node)->None:
    if node.leftnode != None:   
        printTree(node.leftnode)
    if node.rightnode != None:
        printTree(node.rightnode)
    print(node.element)

#main
if __name__ == '__main__':
    root = node(int(input()))
    while 1:
        try:
            element = int(input())
            addTree(element)
        except EOFError: break

    printTree(root)
