
#Problem: https://leetcode.com/problems/number-of-recent-calls/description/?envType=problem-list-v2&envId=queue







#Solution 1:
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the current request's timestamp to the queue
        self.requests.append(t)
        
        # Remove all requests that are older than t - 3000
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # The number of requests in the queue is the count of recent requests
        return len(self.requests)

# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))     
print(recentCounter.ping(100))   
print(recentCounter.ping(3001))  
print(recentCounter.ping(3002))  

print("=======================================================")
#Solution 2:
class RecentCounter:
    def __init__(self):
        self.requests = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1
        return len(self.requests) - self.start
# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))     
print(recentCounter.ping(100))   
print(recentCounter.ping(3001))  
print(recentCounter.ping(3002))  


print("=======================================================")
#Solution 3:
from collections import deque
class RecentCounter:

    def __init__(self):
        self.deque = deque()
        self.count = 0
        
    def ping(self, t: int) -> int:
        self.count += 1
        while len(self.deque):
            if self.deque[0] >= t - 3000:
                break
            else:
                self.count -= 1
                self.deque.popleft()
        self.deque.append(t)
        return self.count 
# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))     
print(recentCounter.ping(100))   
print(recentCounter.ping(3001))  
print(recentCounter.ping(3002))  


print("=======================================================")
#Solution 4:
class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        # range = [t - 3000, t]
        start = t - 3000
        for i in range(len(self.q)):
            if self.q[i] >= start:
                return len(self.q[i:])
# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))     
print(recentCounter.ping(100))   
print(recentCounter.ping(3001))  
print(recentCounter.ping(3002))  


#Explanation : https://chat.deepseek.com/a/chat/s/70eb35eb-af72-4098-94cc-c9a81245a97e