#Problem : https://leetcode.com/problems/crawler-log-folder/description/?envType=problem-list-v2&envId=stack






#Solution 1
def minOperations(logs):
    depth = 0
    for log in logs:
        if log == "../":
            if depth > 0:
                depth -= 1
        elif log != "./":
            depth += 1
    return depth


logs1 = ["d1/","d2/","../","d21/","./"]
logs2 = ["d1/","d2/","./","d3/","../","d31/"]
logs3 = ["d1/","../","../","../"]

print(minOperations(logs1))
print(minOperations(logs2))
print(minOperations(logs3))

print("====================================================")

#Solution 2
def minOperations(logs):
        layer = 0

        for log in logs:
            if log == '../':
                layer = max(0, layer - 1)
            elif log != './':
                layer += 1

        return layer




logs1 = ["d1/","d2/","../","d21/","./"]
logs2 = ["d1/","d2/","./","d3/","../","d31/"]
logs3 = ["d1/","../","../","../"]

print(minOperations(logs1))
print(minOperations(logs2))
print(minOperations(logs3))


print("====================================================")

#Solution 3
import re

def minOperations(logs):
        depth = 0
        for log in logs:
            if log == '../' and depth > 0:
                depth -= 1
            elif re.match(r"[a-zA-Z0-9]+/", log):
                depth += 1
            elif log == "./":
                continue
        return depth



logs1 = ["d1/","d2/","../","d21/","./"]
logs2 = ["d1/","d2/","./","d3/","../","d31/"]
logs3 = ["d1/","../","../","../"]

print(minOperations(logs1))
print(minOperations(logs2))
print(minOperations(logs3))

print("====================================================")

#Solution 4
def minOperations(logs ):
        stack = []
        for x in logs:
            if x == '../':
                if stack: 
                     stack.pop()   
            elif x == './':                     
                pass
                #continue
            else:
                stack.append(x)
        return len(stack)

logs1 = ["d1/","d2/","../","d21/","./"]
logs2 = ["d1/","d2/","./","d3/","../","d31/"]
logs3 = ["d1/","../","../","../"]

print(minOperations(logs1))
print(minOperations(logs2))
print(minOperations(logs3))


#OR we can use instead of the line pass
#elif log != "./":
#   paths_stack.append(log)





