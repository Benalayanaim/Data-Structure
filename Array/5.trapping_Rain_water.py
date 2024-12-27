
#https://leetcode.com/problems/trapping-rain-water/description/

def trap(height):
    if not height:
        return 0

    n = len(height)
    leftMax = [0] * n
    rightMax = [0] * n

    # Fill leftMax
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])

    # Fill rightMax
    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])

    # Calculate water trapped
    water = 0
    for i in range(n):
        water += max(min(leftMax[i], rightMax[i]) - height[i], 0)

    return water

# Examples
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(trap([4,2,0,3,2,5]))  # Output: 9




#Another solution : https://leetcode.com/problems/trapping-rain-water/solutions/5126477/video-keep-max-height-on-the-both-side/