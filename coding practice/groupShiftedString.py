# 249. Group Shifted String

# Last Updated : 28 Dec, 2024
# Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other.

# Two strings s1 and s2 are called shifted if the following conditions are satisfied:

# s1.length is equal to s2.length
# s1[i] is equal to s2[i] + m for all 1 <= i <= s1.length for a constant integer m. Consider the shifting to be cyclic, that is if s2[i] + m > 'z', then start from 'a' or if s2[i] + m < 'a', then start from 'z'.
# Examples:

# Input: arr[] = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
# Output: [ ["acd", "dfg", "wyz", "yab", "mop"], ["bdfh", "moqs"], ["a", "x"] ]
# Explanation: All shifted strings are grouped together.

# Input: arr = ["geek", "for", "geeks"]
# Output: [["for"], ["geek"], ["geeks"]]

# # -------------------------------------------------------------------------------
# The idea is to generate a unique hash for each group by normalizing the strings. Here normalizing means making the first character of every string equal to 'a' by calculating the required shifts and applying it uniformly to all characters in cyclic fashion.
# Example:  s = "dca", shifts = 'd' - 'a' = 3
# normalized characters: 'd' - 3 = 'a', 'c' - 3 = 'z' and 'a' - 3 = 'x'
# normalized string = "azx"

# The normalized string (hash) represents the shift pattern such that strings with the same pattern have the same hash. We use a hash map to track these hashes, and map them to corresponding groups. For each string, we compute a hash and use it to either create a new group or add the string to an existing group in a single traversal.

# (Relative distance between characters is same so relative distance from a reference(a) is also same) --> used to make hash-key
def groupShiftedString(arr):
    str_map = {}

    for s in arr:
        key = hashvalue(s)

        if key in str_map:
            str_map[key].append(s)
        else:
            str_map[key] = [s]
    
    return [value for value in str_map.values()]

def hashvalue(s):
    shift = ord(s[0]) - 97
    new_s = []
    for c in s:
        shifted_to = (ord(c)-shift)
        if shifted_to < 97:
            shifted_to += 26
        shifted_c = chr(shifted_to)
        new_s.append(shifted_c)
    return "".join(new_s)

arr = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
print(groupShiftedString(arr))

# -------------------------------------------------------------------------------