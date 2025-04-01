
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        oldToNew = {None:None}
        
        # Creating hashmap with old as key and new as val
        cur = head
        while cur:
            new = Node(cur.val)
            oldToNew[cur] =  new
            cur = cur.next

        # Assign .next and .random
        cur = head
        while cur:
            new = oldToNew[cur]
            new.next = oldToNew[cur.next]
            new.random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]
    
##### APPROACH 2 #######


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        # This is space optimization - 1 solution
        # Hint: Add the new LLs right next to the OG LL
        # Add the correct random poiters to new LLs
        # Seperate the new and old LLs

        cur = head
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next

        newHead = Node(0)
        if head and head.next:
            newHead.next = head.next # If we don't point it, how will we return it
        cur = head
        while cur:
            # If random is None, there is no random.next. Also, by default the random is going to be Null
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head

        while cur:
            new = cur.next
            cur.next = new.next
            if new.next:
                new.next = new.next.next
            cur = cur.next
        return newHead.next
    
###### APPROACH 3 #####


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        # This is another logic, space optimization - 2
        # Hint: Store the new copy inside random pointers of OG nodes
        # Store the OG's random in new copy's .next

        cur = head
        while cur:
            new = Node(cur.val, cur.random)
            cur.random = new
            cur = cur.next

        cur = head
        newHead = Node(0)
        if head and head.random:
            newHead = head.random
        else:
            return head

        # Set up .random for the copied nodes
        while cur:
            new = cur.random
            # .random is the key, we need this to be pointing to new node.
            new.random = new.next.random if new.next else None
            cur = cur.next

        cur = head
        while cur:
            new = cur.random
            cur.random = new.next
            new.next = cur.next.random if cur.next else None
            cur = cur.next

        return newHead       