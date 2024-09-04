class MyHashMap:

    def __init__(self):
        self.myBucket = [[]]
        self.myHash = 0

        
    def myHashFunction(self, key: int) -> int:
        return key % 1000
    
    
    def setter(self, key: int, value: int) -> None:
        for a, [b, c] in enumerate(self.myBucket[self.myHash]):
            if b == key:
                self.myBucket[self.myHash][a] = [key, value]
                
    
    def put(self, key: int, value: int) -> None:
        if (self.get(key) != -1):
            self.setter(key, value)
            return
        self.myBucket[self.myHash].append([key, value])        

        
    def get(self, key: int) -> int:
        self.myHash = self.myHashFunction(key)
        while (len(self.myBucket) < self.myHash  + 1):
            self.myBucket.append([])
        for a, [b, c] in enumerate(self.myBucket[self.myHash]):
            if b == key:
                return c
        return -1

    
    def remove(self, key: int) -> None:
        if (self.get(key) == -1):
            return
        for a, [b, c] in enumerate(self.myBucket[self.myHash]):
            if b == key:
                del self.myBucket[self.myHash][a]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)