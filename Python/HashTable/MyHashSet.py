class MyHashSet:

    def __init__(self):
        self.myBucket = [[]]

    def myHashFunction(self, key: int) -> int:
        return key % 1000
    
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        myHash = self.myHashFunction(key)
        self.myBucket[myHash].append(key)

    def remove(self, key: int) -> None:
        if (self.contains(key) == False):
            return
        myHash = self.myHashFunction(key)
        for a, b in enumerate(self.myBucket[myHash]):
            if b == key:
                del self.myBucket[myHash][a]
        

    def contains(self, key: int) -> bool:
        myHash = self.myHashFunction(key)
        while (len(self.myBucket) < myHash  + 1):
            self.myBucket.append([])
        for a in self.myBucket[myHash]:
            if a == key:
                return True
        return (key in self.myBucket[myHash])
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
