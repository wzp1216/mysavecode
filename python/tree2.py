class Node():
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None

class Tree():
    def __init__(self):
        self.root=None

    def level_travel(self):
        if self.root==None:
            return
        queue=[self.root]
        while(queue):
            cur=node=queue.pop(0)
            print(cur.elem)
            if cur.lchild!=None:
                queue.append(cur.lchild)
            if cur.rchild!=None:
                queue.append(cur.rchild)
    
    def add(self,item):
        node=Node(item)
        if self.root==None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur=queue.pop(0)
            if cur.lchild==None:
                cur.lchild=node
                return
            else:
                queue.append(cur.lchild)
            if cur.rchild==None:
                cur.rchild=node
                return
            else:
                queue.append(cur.rchild)
    
if __name__=="__main__":
    t=Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.level_travel()

