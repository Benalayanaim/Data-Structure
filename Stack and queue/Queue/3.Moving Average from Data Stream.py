#Problem : 
# https://leetcode.ca/2016-11-10-346-Moving-Average-from-Data-Stream/
#https://www.youtube.com/watch?v=FFX6bz4RCGU





#Solution1:
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize the MovingAverage object with the specified window size.
        """
        self.size = size
        self.queue = deque()
        self.current_sum = 0  # To keep track of the sum of the current window

    def next(self, val: int) -> float:
        """
        Calculate the moving average of the last 'size' values.
        """
        # Add the new value to the queue and the current sum
        self.queue.append(val)
        self.current_sum += val

        # If the queue size exceeds the window size, remove the oldest element
        if len(self.queue) > self.size:
            self.current_sum -= self.queue.popleft()

        # Calculate and return the average
        return self.current_sum / len(self.queue)

# Example usage:
movingAverage = MovingAverage(3)
print(movingAverage.next(1))   
print(movingAverage.next(10))  
print(movingAverage.next(3))   
print(movingAverage.next(5))   



print("=====================================================")

#Solution 2
from collections import deque

class MovingAverage:
    """
    Calculates the moving average of a stream of integers.
    
    Attributes:
    size (int): The size of the window.
    window (deque): A deque to store the last 'size' values of the stream.
    total (float): The sum of the last 'size' values of the stream.
    """
    
    def __init__(self, size: int):
        """
        Initializes the object with the size of the window.
        
        Args:
        size (int): The size of the window.
        """
        self.size = size
        self.window = deque()
        self.total = 0.0

    def next(self, val: int) -> float:
        """
        Returns the moving average of the last 'size' values of the stream.
        
        Args:
        val (int): The next value in the stream.
        
        Returns:
        float: The moving average of the last 'size' values of the stream.
        """
        if len(self.window) == self.size:
            # Remove the oldest value from the window and subtract it from the total
            self.total -= self.window.popleft()
        
        # Add the new value to the window and add it to the total
        self.window.append(val)
        self.total += val
        
        # Calculate and return the moving average
        return self.total / len(self.window)


# Example usage:
if __name__ == "__main__":
    moving_average = MovingAverage(3)
    print(moving_average.next(1))   
    print(moving_average.next(10)) 
    print(moving_average.next(3))   
    print(moving_average.next(5))   


### Explanation : 
"""*   We use a `deque` to store the last `size` values of the stream. This allows us to efficiently remove the oldest value when the window is full.
*   We maintain a `total` variable to store the sum of the last `size` values of the stream. This allows us to calculate the moving average in constant time.
*   In the `next` method, we remove the oldest value from the window if it's full, add the new value to the window, and update the `total`.
*   Finally, we calculate and return the moving average by dividing the `total` by the number of values in the window."""

### we use Object-Oriented Programming (OOP) principles in this solution. Here's how:
"""
1.  **Class**: We define a `MovingAverage` class, which is a fundamental concept in OOP. This class encapsulates the data and behavior related to calculating the moving average.
2.  **Object**: When we create an instance of the `MovingAverage` class, such as `moving_average = MovingAverage(3)`, we create an object that has its own state (attributes) and behavior (methods).
3.  **Attributes (Data Members)**: The `MovingAverage` class has attributes like `size`, `window`, and `total`, which are used to store the state of the object.
4.  **Methods**: The class has methods like `__init__` (constructor) and `next`, which define the behavior of the object. These methods operate on the object's attributes and perform calculations to achieve the desired result.
5.  **Encapsulation**: The `MovingAverage` class encapsulates the data (attributes) and behavior (methods) related to calculating the moving average. This helps to hide the internal implementation details and provides a simple interface for using the class.
6.  **Abstraction**: The `MovingAverage` class provides an abstract representation of the moving average calculation, making it easier to use without worrying about the underlying implementation details.

By using OOP principles, we create a reusable, maintainable, and efficient solution for calculating the moving average from a stream of integers.
"""
