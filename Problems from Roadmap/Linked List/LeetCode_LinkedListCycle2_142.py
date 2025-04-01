# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head):
        kuttyNode = ListNode(0)
        kuttyNode.next = head
        slow, fast = kuttyNode, kuttyNode

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        slow2 = kuttyNode

        if not head or not head.next:
            return None

        while slow:
            if slow2 == slow:
                return slow2
        
            slow2 = slow2.next
            slow = slow.next

        return None
        