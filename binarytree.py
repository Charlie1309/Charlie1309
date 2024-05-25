class Node:
    tree = []

    def __init__(self, data):
        self.leftpointer = -1
        self.data = data
        self.rightpointer = -1

    @classmethod
    def initialize(cls):
        global nullpointer, freepointer, rootpointer
        nullpointer = -1
        freepointer = 0
        rootpointer = -1
        cls.tree = [Node(i) for i in range(6)] 
        for i in range(6):
            cls.tree[i].leftpointer = i + 1
        cls.tree[5].leftpointer = nullpointer

    def insert_item(self, newitem):
        global nullpointer, rootpointer, freepointer
        if freepointer == nullpointer:
            print("There is no space")
        else:
            newnodepointer = freepointer
            freepointer = self.tree[freepointer].leftpointer
            self.tree[newnodepointer].data = newitem
            self.tree[newnodepointer].leftpointer = nullpointer
            self.tree[newnodepointer].rightpointer = nullpointer
            if rootpointer == nullpointer:
                rootpointer = newnodepointer
            else:
                thisnodepointer = rootpointer
                while thisnodepointer != nullpointer:
                    previouspointer = thisnodepointer
                    if self.tree[thisnodepointer].data > newitem:
                        left = True
                        thisnodepointer = self.tree[thisnodepointer].leftpointer
                    else:
                        left = False
                        thisnodepointer = self.tree[thisnodepointer].rightpointer
                if left:
                    self.tree[previouspointer].leftpointer = newnodepointer
                else:
                    self.tree[previouspointer].rightpointer = newnodepointer

    def print_tree(self, node_pointer):
        if node_pointer != -1:
            self.print_tree(self.tree[node_pointer].leftpointer)
            print("Node data:", self.tree[node_pointer].data)
            self.print_tree(self.tree[node_pointer].rightpointer)


# Example usage
Node.initialize()
root_node = Node.tree[rootpointer]

# Inserting items
root_node.insert_item(10)
root_node.insert_item(5)
root_node.insert_item(15)
root_node.insert_item(7)

# Displaying the contents of the tree
print("Contents of the tree:")
root_node.print_tree(rootpointer)
