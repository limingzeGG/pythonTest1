class Node(object):
    def __init__(self,elem=-1,lchild=None,rchild=Node):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    