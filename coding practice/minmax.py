import math

def minmax_element_with_min_compare(a):
    n = len(a)
    mn = float('inf')
    mx = float('-inf')

    if n % 2 == 0:              #for even, every element has its pair, while in odd, 1 needs to be adjusted
        if (a[0]>a[1]):
            mn, mx = a[1],a[0]
        else:
            mn, mx = a[0],a[1]
        i = 2
    else:
        mn, mx = a[0]
        i = 1

    for i in range(n-1):
        if(a[i]>a[i+1]):
            mn = min(mn,a[i+1])     #for every pair, there are 3 comparisons, so total comparisons 1.5n (not 2n)
            mx = max(mx,a[i])
        else:
            mn = min(mn,a[i])
            mx = max(mx,a[i+1])
        i += 2

    return mn,mx
        
    
    
a = [3,5,4,3,5,3,3,2,4,6]
min, max = minmax_element_with_min_compare(a)
print(min,max)