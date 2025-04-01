# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        kuttyNode = ListNode()
        kuttyNode.next = head
        L = R = kuttyNode

        i = 0
        while i <= n: 
            R = R.next
            i += 1

        while R:
            L = L.next
            R = R.next

        L.next = L.next.next
        return kuttyNode.next