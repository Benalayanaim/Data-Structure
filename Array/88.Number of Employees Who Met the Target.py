#Problem 
#https://leetcode.com/problems/number-of-employees-who-met-the-target/description/?envType=problem-list-v2&envId=array






#Solution 1:

def numberOfEmployeesWhoMetTarget(hours, target):
        output = 0
        for i in hours:
            if i >= target:
                output += 1
                
        return output  


hours = [0,1,2,3,4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))

hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours, target))


"""Approach
1/ Initialize a counter to keep track of employees meeting the target.
2/ Iterate through the list hours and check if each value is greater than or equal to target.
3/ If the condition is met, increment the counter.
4/ Return the final count."""

print("==============================================================")

#Solution 2:

def numberOfEmployeesWhoMetTarget(hours, target):
        result = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                result += 1
        return result   

hours = [0,1,2,3,4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))

hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours, target))


print("==============================================================")

#Solution 3:

from bisect import bisect_left
def numberOfEmployeesWhoMetTarget(hours, target):
        employee = sorted(hours)
        return len(hours) - bisect_left(employee, target)

hours = [0,1,2,3,4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))

hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours, target))


print("==============================================================")

#Solution4:

def numberOfEmployeesWhoMetTarget(hours, target):
        return sum(h >= target for h in hours)


hours = [0,1,2,3,4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))

hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours, target))