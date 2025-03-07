class MyHashSet:
    #Approach 1
    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.add(key)
        return None

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)
        return None

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False
    
    #Approach 2
    class LinkedList:
        def __init__(self, key):
            self.key = key
            self.next = None

    class MyHashSet:
        def __init__(self):
            self.hashset = [LinkedList(0) for i in range(10000)]

        def add(self, key: int) -> None:
            #Add the node with key
            cur = self.hashset[key % len(self.hashset)]
            while cur.next:
                if cur.next.key == key:
                    return
                cur = cur.next
            cur.next = LinkedList(key)

        def remove(self, key: int) -> None:
            cur = self.hashset[key % len(self.hashset)]
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next

        def contains(self, key: int) -> bool:
            cur = self.hashset[key % len(self.hashset)]
            while cur.next:
                if cur.next.key == key:
                    return True
                cur = cur.next
            return False


    # Your MyHashSet object will be instantiated and called as such:
    # obj = MyHashSet()
    # obj.add(key)
    # obj.remove(key)
    # param_3 = obj.contains(key)