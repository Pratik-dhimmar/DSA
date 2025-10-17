# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 5,370,370/8M
# Acceptance Rate
# 67.3%

# -------------------------------------------------------------------------------

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    alphabet_list = [0] * 26

    for c1, c2 in zip(s, t):
        if c1 != c2:
            alphabet_list[ord(c1) - ord("a")] += 1
            alphabet_list[ord(c2) - ord("a")] -= 1

    for x in alphabet_list:     #  return all(x==0 for x in alphabet_list)
        if x != 0:
            return False
    return True

s = "rat"
t = "car"
print(isAnagram(s,t))

# -------------------------------------------------------------------------------

