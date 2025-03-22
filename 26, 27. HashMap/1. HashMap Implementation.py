class Pair:
    def __init__(self, key, val):
        #Creating a hashmap pair with key and value
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    def hash(self, key):
        #Hash the key(String) into int to access using key as index
        index = 0
        for i in key:
            index += ord(i)
        return index % self.capacity
    def put(self, key, val):
        #This function inserts a key-value pair into a custom hash map using open addressing (linear probing) to handle collisions(two keys hashing to the same index).
        hash_key = self.hash(key)
        pair = Pair(key, val)
        while True:
            if self.map[hash_key] is None:
                self.map[hash_key] = pair
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                print("Map: \n", self.map)
                return
            elif self.map[hash_key].key == key:
                self.map[hash_key].val = val
                print("Map: \n", self.map)
                return
            hash_key += 1
            hash_key = hash_key % self.capacity
      
    def get(self, key):
        #Get the value of the key
        hash_key = self.hash(key)
        print("Get value \n")
        while self.map[hash_key] != None:
            if self.map[hash_key].key == key:
                print(self.map[hash_key].val)
            hash_key += 1
            hash_key = hash_key % self.capacity
        return None
    def rehash(self):
        #Increase the capacity when the map is half full
        self.capacity *= 2
        newMap = [None] * self.capacity

        oldMap = self.map
        self.map = newMap

        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
    def remove(self, key):
        #remove a pair
        if not self.get(key):
            return None
        index = self.hash(key)
        print("Removed ", key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

obj = HashMap()
obj.put("Param", 28)
obj.put("Aananthi", 25)
obj.put("Kuberan", 30)
obj.put("Appa", 29)
obj.put("Amma", 5)

obj.get("Param")
obj.remove("Aananthi")