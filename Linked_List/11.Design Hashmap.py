#Problem 
#https://leetcode.com/problems/design-hashmap/?envType=problem-list-v2&envId=linked-list


"Explanation"
#https://www.youtube.com/watch?v=cNWsgbKwwoU






"Solution1"
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]# read the previous line to understand this line 
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]# read the previous line to understand this line 
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]# read the previous line to understand this line 
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

# Example usage:
myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))    # Output: 1
print(myHashMap.get(3))    # Output: -1
myHashMap.put(2, 1)
print(myHashMap.get(2))    # Output: 1
myHashMap.remove(2)
print(myHashMap.get(2))    # Output: -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


"Solution2"
class MyHashMap:

    def __init__(self):
        # We use 1000 buckets, each bucket is a list of [key, value] pairs.
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]

    def _hash(self, key: int) -> int:
        # Hash function to map the key to a bucket index
        return key % self.bucket_size

    def put(self, key: int, value: int) -> None:
        # Get the bucket index for the key
        index = self._hash(key)
        # Iterate over the bucket and update the value if the key exists
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value  # Update the value if the key exists
                return
        # If the key does not exist, append the key-value pair to the bucket
        self.buckets[index].append([key, value])

    def get(self, key: int) -> int:
        # Get the bucket index for the key
        index = self._hash(key)
        # Iterate over the bucket to find the key and return its value
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if the key is found
        return -1  # Return -1 if the key is not found

    def remove(self, key: int) -> None:
        # Get the bucket index for the key
        index = self._hash(key)
        # Iterate over the bucket and remove the key-value pair if found
        for pair in self.buckets[index]:
            if pair[0] == key:
                self.buckets[index].remove(pair)  # Remove the pair
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



"Solution3"
class MyHashMap:

    def __init__(self):
        self.di = {}
        
    def put(self, key: int, value: int) -> None:
        self.di[key] = value

    def get(self, key: int) -> int:
        if key in self.di:
            return self.di[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.di:
            del self.di[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



"Solution4"
class MyHashMap:

    def __init__(self):
        self.root = {}

    def put(self, key: int, value: int) -> None:
        self.root[key] = value

    def get(self, key: int) -> int:
        return self.root.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.root:
            del self.root[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)




