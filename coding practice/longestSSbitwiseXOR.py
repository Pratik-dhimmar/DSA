# 3702. Longest Subsequence With Non-Zero Bitwise XOR
# Medium

# You are given an integer array nums.

# Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 

# Example 1:

# Input: nums = [1,2,3]

# Output: 2

# Explanation:

# One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

# Example 2:

# Input: nums = [2,3,4]

# Output: 3

# Explanation:

# The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 18,109/53.6K
# Acceptance Rate
# 33.8%

# ---------------------------------------------------------------------------
from functools import reduce
def longestSubsequence( nums: list[int]) -> int:
        n = len(nums)
        if nums.count(0)==n:
            return 0
        res = reduce(lambda x,y:x^y,nums)
        if res != 0:
              return n
        else: return n-1

nums = [2,3,4]
print(longestSubsequence(nums))

# ---------------------------------------------------------------------------