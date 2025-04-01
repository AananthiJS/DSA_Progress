class ListNode:
    def __init__(self, val = "", prev = None, next = None):
        self.val = str(val)
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.kuttyNode = ListNode(homepage)
        self.head, self.tail, self.cur = self.kuttyNode, self.kuttyNode, self.kuttyNode
        self.size = 0

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        if self.kuttyNode.next == None:
            self.kuttyNode.next = newNode
            newNode.prev = self.kuttyNode
            self.tail = newNode
            self.cur = self.tail
            self.size += 1
        else:
            self.cur.next = newNode
            newNode.prev = self.cur
            self.cur = newNode
            self.tail = self.cur
            self.size += 1
        return None
        
    def back(self, steps: int) -> str:
        i = 0
        while i != steps:
            if self.cur != self.head:
                self.cur = self.cur.prev
                i += 1
            else:
                return self.cur.val
                break
        return str(self.cur.val)
        
    def forward(self, steps: int) -> str:
        i = 0
        while i != steps:
            if self.cur != self.tail:
                self.cur = self.cur.next
                i += 1
            else:
                return self.cur.val
                break
        return str(self.cur.val)


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)