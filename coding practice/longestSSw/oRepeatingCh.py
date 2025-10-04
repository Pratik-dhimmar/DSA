# 3. Longest Substring Without Repeating Characters
 
# Medium

# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 8,243,976/21.9M
# Acceptance Rate
# 37.7%
# -----------------------------------------------------------------------------

def lengthOfLongestSubstring( s: str) -> int:
        max_length = 0
        l = 0
        last_seen = {}

        for r,c in enumerate(s):
            if c in last_seen and last_seen[c] >= l:
                l = last_seen[c] + 1
            
            last_seen[c] = r
            max_length = max(max_length,(r-l+1))
        return max_length

s = "pwwkew"
print(lengthOfLongestSubstring(s))

# --------------------------------------------------------------------------------