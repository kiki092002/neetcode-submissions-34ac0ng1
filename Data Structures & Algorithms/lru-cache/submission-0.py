class LRUCache:

    def __init__(self, capacity: int):
       self.arr = [] # [(key,value)]
       self.capacity = capacity

    def get(self, key: int) -> int:
        for i,(k,v) in enumerate(self.arr):
            if k == key:
                self.arr.pop(i) # remove from curr pos
                self.arr.append((k,v)) # add to the end of arr (most recently used)
                return v 
        
        return -1

    def put(self, key: int, value: int) -> None:
        for i,(k,v) in enumerate(self.arr):
            if (k==key):
                self.arr.pop(i)
                break
        self.arr.append((key,value))
        if (self.capacity < len(self.arr)):
            self.arr.pop(0)