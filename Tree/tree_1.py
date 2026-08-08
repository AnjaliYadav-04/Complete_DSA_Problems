class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]

root=Node(1)
node2=Node(2)
node3=Node(3) 
node4=Node(4)
node5=Node(5)
node6=Node(6)
node7=Node(7)

root.children=[node2,node3]
node2.children=[node4,node5]
node5.children=[node6]
node3.children=[node7]

def dfs(node):
    print(node.data)

    for child in node.children:
        dfs(child)       

dfs(root)       