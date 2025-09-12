import math

def is_specialNo(no):
    sum = 0
    for x in str(no):
        sum += math.factorial(int(x))
    return (sum==no)

def is_special(n):
    for x in range(n):
        sum = 0
        for i in str(x):
            sum += math.factorial(int(i))
        if (sum==x): print(x)
        

# no = 1
# print(is_specialNo(no))

is_special(100000)  
# 1
# 2
# 145
# 40585