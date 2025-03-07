class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hashmap = [LinkedList(0, 0) for _ in range(len(self.hashmap))]
        
    def put(self, key: int, value: int) -> None:
        cur = self.hashmap[key % len(self.hashmap)]
        while cur.next:
            cur = cur.next
        cur.next = LinkedList(key, value)
        cur = LinkedList(key, value)

    def get(self, key: int) -> int:
        return None

    def remove(self, key: int) -> None:
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)