"Problem"
#https://leetcode.ca/2016-05-18-170-Two-Sum-III-Data-structure-design/








#Solution 1:
class TwoSum:
    def __init__(self):
        # Dictionary to store the counts of numbers
        self.num_counts = {}

    def add(self, number: int) -> None:
        # Add the number to the dictionary, increment the count if it already exists
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value: int) -> bool:
        # Check for each key in the dictionary if the complement exists
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                # Handle the case where num and complement are the same
                if complement == num and self.num_counts[num] > 1:
                    return True
                elif complement != num:
                    return True
        return False

twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(3)
twoSum.add(5)
print(twoSum.find(4))  
print(twoSum.find(7))
print(twoSum.find(6))  



print("======================================")

#Solution 2:
import collections

class TwoSum:
  def __init__(self):
    self.count = collections.Counter()

  def add(self, number: int) -> None:
    self.count[number] += 1

  def find(self, value: int) -> bool:
    for key, freq in self.count.items():
      remain = value - key
      if key == remain and freq > 1:
        return True
      if key != remain and remain in self.count:
        return True

    return False
  
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(3)
twoSum.add(5)
print(twoSum.find(4))  
print(twoSum.find(7))
print(twoSum.find(6))  



print("======================================")

#Solution 3:

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_counts = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :type number: int
        :rtype: void
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers whose sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                if complement != num or self.num_counts[num] > 1:
                    return True
        return False
        
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(3)
twoSum.add(5)
print(twoSum.find(4))  
print(twoSum.find(7))
print(twoSum.find(6))  



"Fy chat mteiiii"

#Explanation : https://chatgpt.com/c/6783ac0f-dc00-800f-a33e-76f9fadd9d55