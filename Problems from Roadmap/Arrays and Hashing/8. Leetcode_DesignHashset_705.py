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


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)