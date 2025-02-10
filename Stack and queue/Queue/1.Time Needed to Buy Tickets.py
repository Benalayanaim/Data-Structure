#Problem : https://leetcode.com/problems/time-needed-to-buy-tickets/description/?envType=problem-list-v2&envId=array


"""
Overview
We have a queue of people who each want to buy a certain number of tickets. We are given an array where each element represents 
the number of tickets each person wants to buy. We need to find out how much time it will take for the person at a specific position k 
in the queue to finish buying their tickets.

Key Observations:

1/Each person takes exactly 1 second to buy a ticket.
2/A person can only buy 1 ticket at a time before going to the back of the line.
3/Once a person has bought all the tickets they want, they leave the line.
4/The order of people in the line is fixed, meaning the person at the front of the line (position 0) gets served first, 
then the person behind them, and so on."""

#solution 1
def time_needed_to_buy_tickets(tickets, k):
    time = 0  # Initialize total time

    for i in range(len(tickets)):
        # Calculate time taken based on ticket count
        time += min(tickets[i], tickets[k] if i <= k else tickets[k] - 1)
    
    return time

# Example usage
tickets1 = [2, 3, 2]
k1 = 2
print(time_needed_to_buy_tickets(tickets1, k1))  

tickets2 = [5, 1, 1, 1]
k2 = 0
print(time_needed_to_buy_tickets(tickets2, k2)) 





print("==================================================")

#Solution 2:
from collections import deque
def timeRequiredToBuy(tickets, k): 
        queue = deque()

        # Initialize the queue with ticket indices
        for i in range(len(tickets)):
            queue.append(i)

        time = 0

        # Loop until the queue is empty
        while queue:
            # Increment the time counter for each iteration
            time += 1

            # Get the front element of the queue
            front = queue.popleft()

            # Buy a ticket for the front person
            tickets[front] -= 1

            # If person k bought all their tickets, return time
            if k == front and tickets[front] == 0:
                return time

            # Re-add the current index to the queue for the next iteration
            if tickets[front] != 0:
                queue.append(front)

        return time

# Example usage
tickets1 = [2, 3, 2]
k1 = 2
print(time_needed_to_buy_tickets(tickets1, k1))  

tickets2 = [5, 1, 1, 1]
k2 = 0
print(time_needed_to_buy_tickets(tickets2, k2)) 



print("==================================================")

#Solution 3:
def timeRequiredToBuy(tickets, k): 
        total = 0

        for i, x in enumerate(tickets):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total

# Example usage
tickets1 = [2, 3, 2]
k1 = 2
print(time_needed_to_buy_tickets(tickets1, k1))  

tickets2 = [5, 1, 1, 1]
k2 = 0
print(time_needed_to_buy_tickets(tickets2, k2)) 
"""OR:
def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[k], tickets[i])
            else:
                time += min(tickets[k] - 1, tickets[i])

        return time
"""




print("==================================================")

#Solution 2:
def timeRequiredToBuy(tickets, k):
        time = 0
        while tickets[k] > 0:  # Continue until the kth person has finished buying their tickets
            for j in range(len(tickets)):
                if tickets[j] > 0:
                    tickets[j] -= 1
                    time += 1
                if tickets[k] == 0:  # If the kth person is done, return the time
                    return time
                    
# Example usage
tickets1 = [2, 3, 2]
k1 = 2
print(timeRequiredToBuy(tickets1, k1))  

tickets2 = [5, 1, 1, 1]
k2 = 0
print(timeRequiredToBuy(tickets2, k2)) 

"""OR 
def timeRequiredToBuy(tickets, k):
        time = 0
        for i in range(sum(tickets)):
            for j in range(len(tickets)):
                if tickets[j] > 0:
                    tickets[j] -= 1
                    time += 1
                if j == k:
                    if tickets[j] == 0:
                        return time
                        """

#===>"#Explanation fy chat mte3iii li solution hedhi : https://chatgpt.com/c/6793aaf5-be94-800f-98b4-add9411592dd" 




'For the others Solutions'
#Explanation fy chat mteii : https://chatgpt.com/c/67939b5d-0248-800f-8742-37e9ae023d39