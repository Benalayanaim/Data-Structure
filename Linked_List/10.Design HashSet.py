#Problem
#https://leetcode.com/problems/design-hashset/description/?envType=problem-list-v2&envId=linked-list


"Solution 1"
class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)


    def contains(self, key: int) -> bool:
        for i in self.set:
            if i == key:
                return True
        return False

# Example usage:
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))  # Output: True
print(myHashSet.contains(3))  # Output: False
myHashSet.add(2)
print(myHashSet.contains(2))  # Output: True
myHashSet.remove(2)
print(myHashSet.contains(2))  # Output: False

# Example usage2:
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# print(obj.contains(1))  # Should print True
# print(obj.contains(3))  # Should print False
# obj.remove(2)
# print(obj.contains(2))  # Should print False


"Solution 2"
class MyHashSet:

    def __init__(self):
        self.t = set()
        

    def add(self, key: int) -> None:
        self.t.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.t:
            self.t.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.t:
            return True
        else:
            return False
        #OR
        #return key in self.di
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


"Solution 3 o handle collisions using a technique called"#==> chaining.
class MyHashSet:

    def __init__(self):
        # Choose a prime number for better distribution
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]

    def _hash(self, key: int) -> int:
        # Hash function to map the key to a bucket index
        return key % self.bucket_size

    def add(self, key: int) -> None:
        # Get the hash index for the key
        index = self._hash(key)
        # Add the key to the bucket only if it's not already present
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        # Get the hash index for the key
        index = self._hash(key)
        # Remove the key if it exists in the bucket
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        # Get the hash index for the key
        index = self._hash(key)
        # Check if the key exists in the bucket
        return key in self.buckets[index]

# Example usage:
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# print(obj.contains(1))  # Should print True
# print(obj.contains(3))  # Should print False
# obj.remove(2)
# print(obj.contains(2))  # Should print False


"Solution 4 o handle collisions using a"#==>Linked List.

#https://www.youtube.com/watch?v=VymjPQUXjL8




