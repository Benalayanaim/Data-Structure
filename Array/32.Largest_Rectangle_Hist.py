"Problem"
#https://leetcode.com/problems/largest-rectangle-in-histogram/description/



#Solution 1:
def largestRectangleArea(heights):
    n = len(heights)
    max_area = 0

    for i in range(n):
        # Find the range of bars where the height is at least heights[i]
        left = i
        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1
        
        right = i
        while right < n - 1 and heights[right + 1] >= heights[i]:
            right += 1

        # Calculate the area with heights[i] as the shortest bar
        width = right - left + 1
        area = heights[i] * width
        max_area = max(max_area, area)
    
    return max_area



hei = [2,1,5,6,2,3]

print(largestRectangleArea(hei))

hei2 = [2,4]

print(largestRectangleArea(hei2))


print("====================================")

#Solution 2:

def largestRectangleArea1(heights):
    # Add a 0 height bar at the end to process all heights in the stack
    heights.append(0)
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        # If the stack is not empty and the current bar is shorter
        # than the bar at the index on top of the stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]  # Height of the popped bar
            if not stack:                                                 #width = i if not stack else i - stack[-1] - 1  # Calculate width
                width = i 
            else:
                width = i - stack[-1] - 1  # Calculate width
            max_area = max(max_area, height * width)  # Update max area
        stack.append(i)  # Push the current bar index into the stack
    
    return max_area


hei = [2,1,5,6,2,3]

print(largestRectangleArea1(hei))

hei2 = [2,4]

print(largestRectangleArea1(hei2))


print("=================================")

#Solution 3:
def largestRectangleArea2(bars):
        st, res = [], 0
        for bar in bars + [-1]: # add -1 to have an additional iteration
            step = 0
            while st and st[-1][1] >= bar:
                w, h = st.pop()
                step += w
                res = max(res, step * h)

            st.append((step + 1, bar))

        return res
hei = [2,1,5,6,2,3]

print(largestRectangleArea2(hei))

hei2 = [2,4]

print(largestRectangleArea2(hei2))


print("========================================")

#Solution 4 :
def largestRectangleArea3(heights):
        heights.append(0)
        recents = []
        largest_rect = 0
        prev_h = 0
        for i, height in enumerate(heights):
            if height == prev_h:
                continue
            prev_h = height
            cur_i = i
            while recents:
                h, start = recents[-1]
                if h <= height:
                    break
                recents.pop()
                area = (i - start) * h
                cur_i = start
                if area > largest_rect:
                    largest_rect = area
            if not recents or recents[-1][0] != height:
                recents.append((height, cur_i))
        return largest_rect
hei = [2,1,5,6,2,3]

print(largestRectangleArea3(hei))

hei2 = [2,4]

print(largestRectangleArea3(hei2))


#Explanation :
"open the chagpt mte3iiii"
#https://chatgpt.com/c/676e78ce-6414-800f-9a76-8456491599d8