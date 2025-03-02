class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        #Initialising a dummy node
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index):
        i = 0
        temp = self.head
        while i < index:
            temp = temp.next
            i += 1
        if temp and temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next

    def printList(self):
        curr = self.head.next
        while curr:
            print(curr.val, "->", end="")
            curr = curr.next
        print()

obj = LinkedList()
obj.insertEnd(1)
obj.printList()
obj.insertEnd(2)
obj.printList()
obj.insertEnd(3)
obj.printList()
obj.insertEnd(4)
obj.printList()
obj.remove(2)
obj.printList()
