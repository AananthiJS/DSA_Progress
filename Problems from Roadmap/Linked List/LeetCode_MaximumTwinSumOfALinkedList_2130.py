###### APPROACH 1 ##########
# I used hashmap to store the val of first half of LL
# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:
        slow, fast = head, head
        visitedNodes = {}
        key = 0

        while fast and fast.next:
            visitedNodes[key] = slow.val
            key += 1
            slow = slow.next
            fast = fast.next.next
        
        length = (key) * 2
        maximum = 0

        for i in range(key, length):
            if slow:
                high = slow.val + visitedNodes[length - 1 - i]
                maximum = max(maximum, high)
                slow = slow.next

        return maximum
    
####### APPROACH 2 #######
# Reevrsing the second half of the list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of LL
        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            newNode = cur.next
            cur.next = prev
            prev = cur
            cur = newNode

        # Sum the values and return the max
        cur = head
        res = 0
        while prev:
            res = max(res, cur.val + prev.val)
            prev, cur = prev.next, cur.next
        
        return res
    
######## APPROACH 3 ##########

# Reversing first half of the list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHead = slow
        cur = head
        prev = None
        while cur != slow:
            newNode = cur.next
            cur.next = prev
            prev = cur
            cur = newNode

        res = 0
        while prev and secondHead:
            res = max(res, prev.val + secondHead.val)
            prev, secondHead = prev.next, secondHead.next

        return res