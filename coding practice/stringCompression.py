def string_compression(s):
    n = len(s)
    count = 1
    for i in range(n-1):
        
        if(s[i] == s[i+1]):
            count += 1
        else:
            print(f"{s[i]}{count}",end='')
            count = 1
    print(f"{s[n-1]}{count}",end='')
        


s = 'aabbsssaaaccbbb'
string_compression(s)
# print(s.count('a'))
# s = set(s)
# print(set(s))
# print()