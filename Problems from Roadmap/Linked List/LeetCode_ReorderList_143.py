# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Logic: Go half way through the LL
        # separate the other half, change the pointer
        # Merge the LLs

        # Slow and fast pointers to find the half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            newNode = second.next
            second.next = prev
            prev = second
            second = newNode

        cur = head
        second = prev
        while second:
            temp2 = second.next
            temp1 = cur.next

            cur.next = second
            second.next = temp1

            cur = temp1
            second = temp2