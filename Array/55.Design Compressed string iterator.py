#Problem
#https://leetcode.ca/2017-07-26-604-Design-Compressed-String-Iterator/
#https://www.youtube.com/watch?v=y6d0nBz99Ao&t=483s





#Solution 1

class StringIterator:
    def __init__(self, compressedString: str):
        # Parse the compressed string
        self.data = []
        i = 0
        while i < len(compressedString):
            # Extract character
            char = compressedString[i]
            i += 1
            # Extract number
            num_start = i
            while i < len(compressedString) and compressedString[i].isdigit():
                i += 1
            count = int(compressedString[num_start:i])
            self.data.append((char, count))
        
        self.index = 0  # Pointer to the current character
        self.remaining = 0  # Remaining count for the current character

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        # If no remaining count, move to the next character
        if self.remaining == 0:
            char, count = self.data[self.index]
            self.remaining = count
            self.index += 1
        
        self.remaining -= 1
        return self.data[self.index - 1][0]

    def hasNext(self) -> bool:
        return self.index < len(self.data) or self.remaining > 0


["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
stringIterator = StringIterator("L1e2t1C1o1d1e1")

print(stringIterator.next())  # Returns "L"
print(stringIterator.next())  # Returns "e"
print(stringIterator.next())  # Returns "e"
print(stringIterator.next())  # Returns "t"
print(stringIterator.next())  # Returns "C"
print(stringIterator.next())  # Returns "o"
print(stringIterator.hasNext())  # Returns True
print(stringIterator.next())  # Returns "d"
print(stringIterator.hasNext())  # Returns True


print("====================================================")

#Solution 2
class StringIterator:

    def __init__(self, compressedString: str):
        """Initializes the StringIterator object with a compressed string."""
        self.compressed_string = compressedString
        self.index = 0
        self.current_char = ""
        self.current_count = 0

    def next(self) -> str:
        """Returns the next character if the original string still has uncompressed characters, otherwise returns a white space."""
        if not self.hasNext():
            return " "

        # If the current character count is greater than 0, return the current character
        if self.current_count > 0:
            self.current_count -= 1
            return self.current_char

        # Find the next character and its count in the compressed string
        while self.index < len(self.compressed_string):
            char = self.compressed_string[self.index]
            self.index += 1
            count = ""
            while self.index < len(self.compressed_string) and self.compressed_string[self.index].isdigit():
                count += self.compressed_string[self.index]
                self.index += 1
            self.current_char = char
            self.current_count = int(count) - 1
            return char

    def hasNext(self) -> bool:
        """Returns True if there is any letter that needs to be uncompressed in the original string, otherwise returns False."""
        # If the current character count is greater than 0, return True
        if self.current_count > 0:
            return True

        # If the compressed string has been fully processed, return False
        if self.index >= len(self.compressed_string):
            return False

        # Check if there are any remaining characters in the compressed string
        return self.index < len(self.compressed_string)


# Example usage
stringIterator = StringIterator("L1e2t1C1o1d1e1")
print(stringIterator.next())  # Output: "L"
print(stringIterator.next())  # Output: "e"
print(stringIterator.next())  # Output: "e"
print(stringIterator.next())  # Output: "t"
print(stringIterator.next())  # Output: "C"
print(stringIterator.next())  # Output: "o"
print(stringIterator.hasNext())  # Output: True
print(stringIterator.next())  # Output: "d"
print(stringIterator.hasNext())  # Output: True



"""Explanation :
The problem requires designing a data structure, specifically a compressed string iterator, to handle compressed strings. 
The compressed strings are in the form of each letter followed by a positive integer representing the number of times 
this letter exists in the original uncompressed string.

For example, the compressed string "L1e2t1C1o1d1e1" represents the uncompressed string "LetCodee".

**Class Methods**

The `StringIterator` class should have two main methods:

1.  **next()**: Returns the next character if the original string still has uncompressed characters. If there are no more characters, it returns a white space.
2.  **hasNext()**: Returns `True` if there is any letter that needs to be uncompressed in the original string. Otherwise, it returns `False`.


In this solution, the `StringIterator` class is initialized with a compressed string. 
===>The `next()` method returns the next character if the original string still has uncompressed characters; otherwise, it returns a white space. 
===>The `hasNext()` method checks if there is any letter that needs to be uncompressed in the original string and returns`True` 
if there is, and `False` otherwise. The class keeps track of the current character and its count, 
as well as the current index in the compressed string.
"""



#OOP Technique used in this solution :
"""
The solution uses several Object-Oriented Programming (OOP) concepts:

1.  **Encapsulation**: The `StringIterator` class encapsulates the compressed string, index, current character, and current count. This means that these data members are hidden from the outside world, and access to them is controlled through public methods (`next()` and `hasNext()`).
2.  **Abstraction**: The `StringIterator` class provides an abstract view of the compressed string, allowing users to interact with it without worrying about the implementation details. The class hides the complexity of iterating over the compressed string, providing a simple interface for users.
3.  **Statefulness**: The `StringIterator` class maintains its state between method calls. The `index`, `current_char`, and `current_count` attributes retain their values between calls to `next()` and `hasNext()`, allowing the class to keep track of its position in the compressed string.
4.  **Single Responsibility Principle (SRP)**: The `StringIterator` class has a single responsibility: to iterate over a compressed string. This makes the class easy to understand, maintain, and modify.

However, the solution does not explicitly demonstrate other OOP concepts like:

*   **Inheritance**: The `StringIterator` class does not inherit from another class.
*   **Polymorphism**: The `StringIterator` class does not override any methods from a parent class, and it does not provide multiple implementations of a method.
*   **Composition**: The `StringIterator` class does not contain other objects as its attributes.

The OOP style used in this solution can be characterized as **straightforward object-oriented programming**, where a single class encapsulates data and behavior, providing a simple and easy-to-use interface for users.

**Design Pattern:**

The solution implements the **Iterator Design Pattern**, which provides a way to access the elements of a collection (in this case, the compressed string) without exposing its underlying representation. The `StringIterator` class acts as an iterator, allowing users to iterate over the compressed string without worrying about the implementation details"""



