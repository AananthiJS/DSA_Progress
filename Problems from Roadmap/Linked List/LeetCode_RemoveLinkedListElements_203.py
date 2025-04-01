# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead

        while cur and cur.next:
            if  val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur =  cur.next

        return dummyHead.next