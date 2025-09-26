# 166. Fraction to Recurring Decimal
# Medium

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
 

# Constraints:

# -231 <= numerator, denominator <= 231 - 1
# denominator != 0
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 337,874/1.1M
# Acceptance Rate
# 29.9%

def fractionToDecimal(self,numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        ans = []
        if (numerator<0) ^ (denominator<0):
            ans.append("-")
        n = abs(numerator)
        d = abs(denominator)
        a, r = divmod(n, d)
        ans.append(str(a))
        # for whole part
        if r == 0:
            return "".join(ans)
        # for decimal part
        ans.append(".")
        rmap = {}
        while r != 0:
            if r in rmap:
                ans.insert(rmap[r], "(")
                ans.append(")")
                return "".join(ans)
            rmap[r] = len(ans)  # last position
            r = r * 10
            a, r = divmod(r, d)
            ans.append(str(a))
        return "".join(ans)
            