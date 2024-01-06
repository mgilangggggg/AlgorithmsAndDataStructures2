class Node :
    def _init_(self, dataBaru) :
        self.left = None
        self.right = None
        self.data = dataBaru

    def insert (self, data) :
        if self.data is None :
            self.data = data
        else :
            if data < self.data :
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.insert (data)
            elif data > self.data :
                if self.right is None :
                    self.right = Node(data)
                else :
                    self.right.insert (data)
            elif data == self.data :
                print('Data Sudah Ada')


    # Pre-Order : Node -> Left -> Right 
    def PreOrderTraversal(self, root) :
        out = []
        if root :
            out.append(root.data)
            out = out + self.PreOrderTraversal(root.left)
            out = out + self.PreOrderTraversal(root.right)
        return out


    # In-Order : Left -> Node -> Right
    def InOrderTraversal(self, root) :
        out = []
        if root :
            out = out + self.InOrderTraversal(root.left)
            out.append(root.data)
            out = out + self.InOrderTraversal(root.right)
        return out


    # Post-Order : Left -> Right -> Node
    def PostOrderTraversal(self, root) :
        out = []
        if root :
            out = out + self.PostOrderTraversal(root.left)
            out.append(root.data)
            out = out + self.PostOrderTraversal(root.right)
        return out


tree = Node('H')
tree.insert('A')
tree.insert('K')
tree.insert('C')
tree.insert('B')
tree.insert('L')
tree.insert('J')

print('Pre-Order Traversal')
print(tree.PreOrderTraversal(tree))

print('In-Order Traversal')
print(tree.InOrderTraversal(tree))

print('In-Order Traversal')
print(tree.PostOrderTraversal(tree))