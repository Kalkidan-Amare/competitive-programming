class Node:
    def __init__(self,value=0):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        temp = self.dummy
        for i in range(index+1):
            temp = temp.next
            if not temp:
                return -1
        return temp.val     

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.dummy.next
        self.dummy.next = newnode

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        temp = self.dummy
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        temp = self.dummy
        for i in range(index):
            temp = temp.next
            if not temp:
                return
        newnode.next = temp.next
        temp.next = newnode

    def deleteAtIndex(self, index: int) -> None:
        temp = self.dummy
        for i in range(index):
            temp = temp.next
            if not temp.next:
                return
        temp.next = temp.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)