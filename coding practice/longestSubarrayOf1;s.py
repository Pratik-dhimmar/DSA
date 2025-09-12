# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1], [1,1,0,0,1,1,1,0,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

def longestSubarrayOf1(num:list)->int:
    left = 0
    # previousZero = 0
    previousZero = -1
    # count = 0
    # flag = 1
    maxlength = float('-inf')

    for i,rightNum in enumerate(num):
        if rightNum == 0:
            # count += 1
            # if (flag): previousZero,flag = i , 0
            # if count > 1:
                left = previousZero + 1
                previousZero = i
                # count -= 1
        maxlength = max(maxlength, i - left )
    print(i,left)
    print(num[left:i+1])
    return maxlength

# num =  [1,1,0,0,1,1,1,0,1]
# ans = longestSubarrayOf1(num)
# print(ans)

# -------------------------------------------------------------------------------

# 1004. Max Consecutive Ones III
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    zero = 0
    maxlength = float("-inf")

    for i,value in enumerate(nums):
        if value == 0:
           zero += 1
        if zero > k:
            if nums[left] == 0:
                  zero -= 1
            left += 1
             
        maxlength = max(maxlength,i-left+1)
    return maxlength

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3           
ans1 = longestOnes(nums,k)
print(ans1)
