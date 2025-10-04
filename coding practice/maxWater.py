# 11. Container With Most Water
# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4,575,785/7.8M
# Acceptance Rate
# 58.6%
# --------------------------------------------------------------

def maxArea( height: list[int]) -> int:
        l = 0
        max_area = 0
        r = len(height) - 1

        while l < r:
            cur_area = (r-l)*min(height[l],height[r])
            max_area = max(max_area,cur_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# --------------------------------------------------------------