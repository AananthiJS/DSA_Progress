# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        i = num1 = 0
        while l1:
            num1 += l1.val * (10 ** i)
            i += 1
            l1 = l1.next

        i = num2 = 0
        while l2:
            num2 += l2.val * (10 ** i)
            i += 1
            l2 = l2.next

        num = num1 + num2

        kuttyNode = ListNode()
        cur = kuttyNode

        if num == 0:
            return kuttyNode

        while num > 0:
            value = num % 10
            num = num // 10
            newNode = ListNode(value)
            cur.next = newNode
            cur = cur.next

        return kuttyNode.next