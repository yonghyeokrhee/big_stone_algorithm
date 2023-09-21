from sys import setrecursionlimit
setrecursionlimit(10000)

class Node:
    def __init__(self, x, y, num):
        self.left = None
        self.right = None
        self.x = x
        self.y = y 
        self.num = num

        
root = None

def binaryTree(root, x, y, num):
    
    if x < root.x:
        if root.left == None:
            root.left = Node(x, y, num)
            return 
        else:
            binaryTree(root.left, x, y, num)
        
        
    elif x > root.x:
        if root.right == None:
            root.right = Node(x, y, num)
            return 
        else:
            binaryTree(root.right, x, y, num)
            
def preOrder(root, tmp):
    
    tmp.append(root.num)
    
    if root.left != None:
        preOrder(root.left, tmp)
    
    if root.right != None:
        preOrder(root.right, tmp)
        

def postOrder(root, tmp):
    
    
    if root.left != None:
        postOrder(root.left, tmp)
        
    if root.right != None:
        postOrder(root.right, tmp)
        
    tmp.append(root.num)
    
        
        
def solution(nodeinfo):
    answer = []
    root = None

    nodes = [] 

    for i in range(len(nodeinfo)):
        nodes.append((nodeinfo[i][0], nodeinfo[i][1], i+1))
    
    nodes.sort(key=lambda x:(-x[1], x[0]))
    
    for i in range(len(nodes)): 
    
        x, y, num = nodes[i][0], nodes[i][1], nodes[i][2] 
    
        if i == 0:
            root = Node(x, y, num)
        
        else:
            binaryTree(root, x, y, num)
    
    tmp1 = [] 
    preOrder(root, tmp1)
    answer.append(tmp1)
    tmp2 = [] 
    postOrder(root, tmp2)
    answer.append(tmp2)
    
    return answer
