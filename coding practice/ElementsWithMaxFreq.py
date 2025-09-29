# 3005. Count Elements With Maximum Frequency
# Easy

# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.

 

# Example 1:

# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 386,075/482.7K
# Acceptance Rate
# 80.0%
# --------------------------------------------------------------------------------
# def maxFrequencyElements(nums: list[int]) -> int:
#     d = {}
#     res = 0
#     for x in nums:
#             d[x] = d.get(x,0) + 1
    
#     maxFreq = max(d.values())
#     elements = 0
#     # elements = d.values().count(maxFreq)      # d.values() give view not list so its not iterable. Need to convert into list
#     for x in d.values():
#           if x == maxFreq:
#             elements += 1

#     res = maxFreq*elements
#     return res 

# nums =  [1,2,3,4,5]
# a = maxFrequencyElements(nums)
# print(a)
# ------------------------------------------------------------------------------------------------
from collections import defaultdict
def maxFrequencyElements(nums: list[int]) -> int:
    d = defaultdict(int)
    maxf = 0
    totalElements = 0
    for num in nums:
        d[num] += 1
        f = d[num]
        if f>maxf:
            maxf = f
            totalElements = d[num]
        elif f == maxf:
             totalElements += maxf
    
    return totalElements

nums =  [1,2,3,4,5]
a = maxFrequencyElements(nums)
print(a) 
# ----------------------------------------------------------------------      