# from collections import Counter

def first_non_repeating_char(s):
    n = len(s)
    for i in range(n-2):
        if(s[i] !=s[i+1] and s[i+1] != s[i+2]) :
            return s[i+1]
        
p=first_non_repeating_char('aaaabbbbcdeeee')
print(p)
# s = 'aaabbssbbbdbttg'
# c = Counter(s)
# print(c)