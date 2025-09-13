# 3677. Count Binary Palindromic Numbers
# Hard

# You are given a non-negative integer n.

# A non-negative integer is called binary-palindromic if its binary representation (written without leading zeros) reads the same forward and backward.

# Return the number of integers k such that 0 <= k <= n and the binary representation of k is a palindrome.

# Note: The number 0 is considered binary-palindromic, and its representation is "0".

 

# Example 1:

# Input: n = 9

# Output: 6

# Explanation:

# The integers k in the range [0, 9] whose binary representations are palindromes are:

# 0 → "0"
# 1 → "1"
# 3 → "11"
# 5 → "101"
# 7 → "111"
# 9 → "1001"
# All other values in [0, 9] have non-palindromic binary forms. Therefore, the count is 6.

# Example 2:

# Input: n = 0

# Output: 1

# Explanation:

# Since "0" is a palindrome, the count is 1.

 

# Constraints:

# 0 <= n <= 1015
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 5,310/25.4K
# Acceptance Rate
# 20.9%
# (TIME LIMIT EXCEEDED)------------------------------------------------------------------------------
import math
# def countBinaryPalindromes( n: int) -> int:
#     if n==0: return 1
#     if n==1: return 2
#     if n==2: return 2
#     if n==3: return 3
#     #count palindromic nos upto the No which is nearest power of 2
#     nearest_power = int(math.log(n,2))
#     print(f"NEAREST POWER:{nearest_power}")
#     res = sequenceNo(nearest_power - 1)         # used chapGPT for general term of the sequence
    
#     # alternate way ----------------
#     # res = 3
#     # for i in range(3,nearest_power+1):
#     #     x = math.ceil((i-2)/2)
#     #     res += round(math.pow(2,x))

#     nearestNo = round(math.pow(2,nearest_power))    #as sometimes math.pow doesn't give exact no, but nearest floating point no
#     print(f"NEAREST NO:{nearestNo}")
#     if n <= nearestNo:
#         return res
#     for i in range(nearestNo+1,n+1,2):  #only check for odd nos
#         # binaryNo = binary(i)
#         binaryString = bin(i)[2:]       # it's very efficient 

#         is_palindrome = 1
#         for i in range(len(binaryString)//2):
#             if binaryString[i] != binaryString[len(binaryString)-1-i]:
#                 is_palindrome = 0
#                 break
#         if is_palindrome:
#         # if is_palindrome(binaryNo):
#             res += 1
#     return res

# def binary(n):
#     l = []
#     while(n>=0):
#         if n==0 or n==1: 
#             l.append(1) 
#             return l
#         l.append(n%2)
#         n = n//2

# def is_palindrome(n):
#     for i in range(len(n)//2):
#         if n[i] != n[len(n)-1-i]:
#             return False
#     return True

# def sequenceNo(n):
#     if n%2 == 0:
#         x = n//2
#         print(x)
#         return (3*round(math.pow(2,x))-1)
#     else:
#         x = (n+3)//2
#         print(x)
#         return (round(math.pow(2,x))-1)

# # print(binary(10))
# # print(countBinaryPalindromes(67108863))

def countBinaryPalindromes1( n: int) -> int:
    if n == 0: return 1
    binaryString = bin(n)[2:]
    binaryNo = [int(x) for x in binaryString]
    print(binaryNo)
    n = len(binaryNo)
    res = 1         # for case 0

    # count palindromes upto n-1 length 
    for i in range(1,n):
        # x = round(math.pow(2,math.ceil(i/2)-1))
        x = 1<<(math.ceil(i/2)-1)
        res += x
        print(i,x,res)

    # count palindromes of (length n) upto n
    half = math.ceil(n/2)
    for i in range(1,half):
        if binaryNo[i] == 1:    # I can flip 1 to 0
            # x = round(math.pow(2,half-1-i))
            x = 1<<(half-1-i)
            res += x
            print(i,x,res)

    # check if n's half is palindrome or not
    left = binaryNo[:half]
    right = binaryNo[-half:]
    if left[::-1]<=right:
        res += 1
    return res


print(countBinaryPalindromes1(10))







