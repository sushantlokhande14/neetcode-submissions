class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = []

    def get(self, key: int) -> int:
        
        for i ,(k,v) in enumerate(self.cache): 
            if k == key :
                self.cache.pop(i)
                self.cache.insert(0, (k,v))
                return v 
        return -1 

    def put(self, key: int, value: int) -> None:
        for i, (k,v) in enumerate(self.cache):
            if k == key : 
                self.cache.pop(i)
                self.cache.insert(0, (key, value))
                return 
            
        if len(self.cache) == self.capacity : 
            self.cache.pop()
            
        self.cache.insert(0, (key,value))
        
