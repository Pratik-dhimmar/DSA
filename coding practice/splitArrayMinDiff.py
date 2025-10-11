# 3698. Split Array With Minimum Difference
# Medium

# You are given an integer array nums.

# Split the array into exactly two subarrays, left and right, such that left is strictly increasing and right is strictly decreasing.

# Return the minimum possible absolute difference between the sums of left and right. If no valid split exists, return -1.

 

# Example 1:

# Input: nums = [1,3,2]

# Output: 2

# Explanation:

# i	left	right	Validity	left sum	right sum	Absolute difference
# 0	[1]	[3, 2]	Yes	1	5	|1 - 5| = 4
# 1	[1, 3]	[2]	Yes	4	2	|4 - 2| = 2
# Thus, the minimum absolute difference is 2.

# Example 2:

# Input: nums = [1,2,4,3]

# Output: 4

# Explanation:

# i	left	right	Validity	left sum	right sum	Absolute difference
# 0	[1]	[2, 4, 3]	No	1	9	-
# 1	[1, 2]	[4, 3]	Yes	3	7	|3 - 7| = 4
# 2	[1, 2, 4]	[3]	Yes	7	3	|7 - 3| = 4
# Thus, the minimum absolute difference is 4.

# Example 3:

# Input: nums = [3,1,2]

# Output: -1

# Explanation:

# No valid split exists, so the answer is -1.

 

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i] <= 105
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 24,718/95.1K
# Acceptance Rate
# 26.0%

# -------------------------------------------------------------------

# def splitArray( nums: list[int]) -> int:
#     n = len(nums)
#     # edge case (n = 2)
#     if n == 2:
#         return abs(nums[0]-nums[1])
    
#     # find peak element
#     peak = -1
#     for i,no in enumerate(nums):
#         if no > peak:
#             peak = no
#             peak_count = 0
#             peak_idx = i
#         if no == peak:
#             peak_count += 1

#     if peak_count > 2:
#         return -1    

#     # strictly increasing (start,peak)
#     i = 1
#     cur = nums[i]
#     while(i < peak_idx):
#         l = nums[i-1]
#         r = nums[i+1]
#         if not (l < cur  and cur < r) :
#             print('l')
#             return -1   
#         i += 1
#         cur = nums[i] 

#     # strictly decreasing (peak,end)
#     if peak_idx != n-1:     # only possible when peak isn't the last element
#         i = peak_idx + 1   
#         cur = nums[i] 
#         while (i < n-1):
#             l = nums[i-1]
#             r = nums[i+1]
#             if not (l >= cur  and cur > r) :    # >= for peak_count = 2
#                 print('r',cur)
#                 return -1   
#             i += 1
#             cur = nums[i]        

#     # find absolute diff
#     left_sum = sum(nums[:peak_idx + 1])
#     right_sum = sum(nums[peak_idx + 1:])

    
#     diff1 = abs(left_sum - right_sum)
#     if peak_count == 2:
#         return diff1
    
#     # 2 possibilities when peak_count = 1 
#     left_sum -= nums[peak_idx]      # same as sum(nums[:peak_idx])
#     right_sum += nums[peak_idx]     # same as sum(nums[peak_idx:])
#     diff2 = abs(left_sum - right_sum)

#     return min(diff1,diff2)

# nums = [1,2,3,4,4,1]
# print(splitArray(nums))
 # -------------------------------------------------------------------
def splitArray( nums: list[int]) -> int:
    n = len(nums)
    l = 0
    r = n-1
    lsum, rsum = 0, 0

    # computing strictly increasing/decreasing sum
    while(l<n-1 and nums[l]<nums[l+1]):
        lsum += nums[l]
        l += 1
    while(r>0 and nums[r]<nums[r-1]):
        rsum += nums[r]
        r -= 1
    
    dif1 = abs(lsum + nums[l] - rsum)
    dif2 = abs(lsum - (nums[l] + rsum))

    # only 1 peak element (2 conditions)
    if (l == r):
        return min(dif1,dif2)
    # two peaks (2 equal elements)
    if(r-l == 1):
        return abs(lsum-rsum)

    return -1

nums = [1,2,3,4,4,1]
print(splitArray(nums))
# -------------------------------------------------------------------