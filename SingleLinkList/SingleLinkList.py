from SingleLinkList import SingleNode

class SingleLinkList(object):
    """单链表实现"""
    def __init__(self):
        self.__head = None
    def is_Empty(self):
        return self.__head == None
    def length(self):
        cur = self.__head
        count = 0
        while cur !=None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self,item):
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        node = SingleNode(item)

        if self.is_Empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        if pos <=0:
            self.add(item)
        elif pos >(self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
                pre.next = node

    def remove(self,item):
        cur = self.__head
        pre = None
        while cur!=None:
            if cur.item ==item:
                if not pre:
                    self.__head == cur.next
                else:
                    pre.next = cur.next
                break

            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while cur !=None:
            if cur.item == item:
                return True
            cur = cur.next

        return False


