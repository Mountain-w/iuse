class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.__length = 0
        self.head = None
        self.tail = None
        self.test = [1, 2, 3, 4]

    def add(self, val):
        newnode = Node(val)
        if self.__length == 0:
            self.head = newnode
            self.tail = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.__length += 1

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        if not self.cur:
            raise StopIteration("Index out of range")
        val = self.cur.val
        self.cur = self.cur.next
        return val

    # def __getitem__(self, item):
    #     print(">>>", item)
    #     if item >= self.__length:
    #         raise IndexError()
    #     cur = self.head
    #     for _ in range(item):
    #         cur = cur.next
    #     return cur.val


linkedlist = LinkedList()
linkedlist.add(10)
linkedlist.add(9)
linkedlist.add(8)
for i in linkedlist:
    print(i)
for i in linkedlist:
    print(i)
