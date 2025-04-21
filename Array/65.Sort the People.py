#Problem : https://leetcode.com/problems/sort-the-people/description/?envType=problem-list-v2&envId=array



#Solution 1:

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    n = len(names)
    mapping = {}  # height -> name (heights are distinct)
    for i in range(n):
        mapping[heights[i]] = names[i]

    heights.sort(reverse=True)
    for i in range(n):
        h = heights[i]
        names[i] = mapping[h]

    return names

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))

names = ["Alice","Bob","bob"]
heights = [155,185,150]
print(sortPeople(names, heights))

""" Explanation :
use hashmap to map person's height to name and then just fill new array with names according to heihts sorting

====>https://assets.leetcode.com/users/images/c3d92a43-636e-4ad9-8d06-f65a1e60597c_1721622829.2827353.png

Coding:
1/Determine the number of elements in names and store it in n.
2/Create a dictionary mapping to store height-name pairs.
3/Populate mapping by iterating through the range n:
    Assign each height as a key and corresponding name as its value.
4/Sort the heights array in descending order.
5/Iterate through the sorted heights:
    Retrieve the name associated with each height from mapping.
    Update the names array with the sorted names based on height.
6/Return the sorted names array.

**Example:** 
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]

### Step 1: Create a dictionary to map heights to names
We create an empty dictionary `mapping` to store the heights as keys and the corresponding names as values. This is possible because the heights are distinct.

```python
mapping = {}  
n = len(names)
for ind in range(n):
    mapping[heights[ind]] = names[ind]
```

**Mapping:**
- `180: Mary`
- `165: John`
- `170: Emma`

### Step 2: Sort the heights in descending order
We sort the `heights` list in descending order.

```python
heights.sort(reverse=True)
```

**Sorted Heights:**
- `[180, 170, 165]`

### Step 3: Update the names list based on the sorted heights
We iterate through the sorted `heights` list and update the `names` list with the corresponding names from the `mapping` dictionary.

```python
for ind in range(n):
    h = heights[ind]
    names[ind] = mapping[h]
```

**Updated Names:**
- For `h = 180`, `names[0] = mapping[180] = Mary`
- For `h = 170`, `names[1] = mapping[170] = Emma`
- For `h = 165`, `names[2] = mapping[165] = John`

### Step 4: Return the sorted names list
The `names` list is now sorted in descending order by height.

**Output:**
- `["Mary","Emma","John"]`

This is the final result, which is returned by the function.
"""


print("====================================")
#Solution 2:
def sortPeople(names, heights):
    # Create a dictionary to store height-name pairs
    height_to_name_map = dict(zip(heights, names))

    sorted_heights = sorted(heights, reverse=True)

    # Create a list of sorted names based on descending heights
    sorted_names = [height_to_name_map[height] for height in sorted_heights]

    return sorted_names 


names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))

names = ["Alice","Bob","bob"]
heights = [155,185,150]
print(sortPeople(names, heights))


print("====================================")
#Solution 3:
def sortPeople(names, heights):
        d={}
        for i in range(len(heights)):
            d[heights[i]]=names[i] # d[key[]]=value[] way to add values to the dictoinary 
            k=sorted(heights)
            k=k[::-1]
            ans=[]
        for i in range(len(k)):
            ans.append(d[k[i]]) 
        return ans

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))

names = ["Alice","Bob","bob"]
heights = [155,185,150]
print(sortPeople(names, heights))


print("==========================================")
#Solution 4:
def sortPeople(names, heights):
        for i in range(len(names)-1):
            for j in range(i+1,len(names)):
                if heights[i] < heights[j]:
                    heights[i],heights[j]=heights[j],heights[i]
                    names[i],names[j]=names[j],names[i]                  
        return names
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))

names = ["Alice","Bob","bob"]
heights = [155,185,150]
print(sortPeople(names, heights))
