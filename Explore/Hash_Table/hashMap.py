class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashMap[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hashMap[key] if (key in self.hashMap) else -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hashMap.pop(key, None)

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)         
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))
