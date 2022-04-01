
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,newdata):
     
        if newdata < self.data:
            if self.left == None:
                self.left = Node(newdata)
            else:
                self.left.insert(newdata)
        else:
            if self.right == None:
                self.right = Node(newdata)
            else:
                self.right.insert(newdata)             


root = Node(1)
root.insert(2)
root.insert(3)

