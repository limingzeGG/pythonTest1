from DLinkList import Node

class SinCycLinkedList(object):

    def __init__(self):
        self.__head = None

    def is_Empty(self):
        return self.__head ==None

    def length(self):
        if self.is_Empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next !=self.__head:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        if self.is_Empty():
            return
        cur = self.__head
        while cur.next !=self.head:
            print(cur.item)
            cur = cur.next

        print("")

    def add(self,item):
        node = Node(item)
        if self.is_Empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            self.__head =node


    def append(self,item):
        node = Node(item)
        if self.is_Empty():
            self.__head = node
            node.next = self.__head

        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self,pos,item):
        if pos <=0:
            self.add(item)
        elif pos >(self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre = self.__head
            while count <(pos - 1):
                count +=1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        if self.is_Empty():
            return
        cur = self.__head
        pre = Node
        while cur.next !=self.__head:
            if cur.item ==item:
                if cur == self.__head:
                    self.__head = cur.next
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next

                    self.__head = cur.next
                    rear.next = self.__head

                else:
                    pre.next = cur.next

                return
            else:
                pre = cur
                cur = cur.next





