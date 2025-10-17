# 49. Group Anagrams
# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4,192,348/5.9M
# Acceptance Rate
# 71.6%

# -------------------------------------------------------------------------------
# sorting -----------------------------------------------------

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = {}

    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = [s]
        else:
            anagram_map[sorted_s].append(s)
        
    return [value for value in anagram_map.values()]


# using char_map ----------------------------------------------

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = {}

    for s in strs:
        # making key(immutable) 
        char_map = [0]*26
        for c in s:
            char_map[ord(c)-97] += 1
        key = tuple(char_map)

        if key not in anagram_map:
            anagram_map[key] = [s]
        else:
            anagram_map[key].append(s)
        
    return [value for value in anagram_map.values()]

# -------------------------------------------------------------------------------
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))