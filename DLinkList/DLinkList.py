from DLinkList import Node

class DLinkList(object):
    def __init__(self):
        self.__head = None

    def is_Empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur!=None:
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
        node = Node(item);
        if self.is_Empty():
            self.__head = node

        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_Empty():
            self.__head = node

        else:
            cur = self.__head
            while cur.next !=None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        if pos <=0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count <(pos - 1):
                count +=1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self,item):
        cur = self.__head
        while cur!=None:
            if cur.item == item:
                if cur ==self.__head:
                    self.__head ==cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item ==item:
                return True
            cur = cur.next

        return False

