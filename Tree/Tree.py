from Tree import Node

class Tree(object):
    def __init__(self,root=None):
        self.root = root

    def add(self,elem):
        node = Node(elem)

        if self.root == None:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild ==None:
                    cur.lchild = node
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self,root):
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)