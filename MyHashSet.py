class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [[False for i in range(1000)] for i in range(1001)]
        self.buckets = 1001
        self.bucketItems = 1000
        
    def bucket(self, key) -> int:
        return key//self.buckets
    
    def bucketItem(self, key) -> int:
        return key%self.bucketItems

    def add(self, key: int) -> None:
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        
        self.set[bucket][bucketItem] = True

    def remove(self, key: int) -> None:
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        if self.set[bucket] is None:
            return
        
        self.set[bucket][bucketItem] = False
        
        
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        if self.set[bucket] is None:
            return False
        return self.set[bucket][bucketItem]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)