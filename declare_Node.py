class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        
def createNode(data):
    newNode= Node(data);
    print(" -Node at ", newNode, "\n -Data- ", newNode.data )

createNode(10);
