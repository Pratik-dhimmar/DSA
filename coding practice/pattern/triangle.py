def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print()

def increasiing_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end = " ")
        print()

def decreasing_triangle(n):        
    for i in range(n):
        for j in range(i,n):
            print("*", end = " ")
        print()
        
def right_increasing_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end = " ")
        for j in range(i+1):
            print("*", end = " ")
        print()

def right_decreasing_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end = " ")
        for j in range(i,n):
            print("*", end = " ")
        print()

def hill(n):
    for i in range(n):
        for j in range(i,n):
            print(" " , end = " ") 
        for j in range(i+1):
            print("*", end = " ")
        for j in range(i):
            # if (j == 0 ): continue
            print("*", end = " ")
        print()

def reverse_hill(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end = " ")
        for j in range(i,n):
            print("*", end = " ")
        # for j in range(i,n-1):          # if u want to do 1 less,(in column) then change in 2nd condition (i.e. n-1, ...) 
            # if (j == 0): continue       # j == 0 occurs only 1 time when i = 0
            if (j == n-1): continue
            print("*", end = " ")
        print()

def dimond(n):
    for i in range(n):
  # for i in range(n-1):                # we can perform it to n-1 to omit last row, then we can use range(n) in 2nd loop
        for j in range(i,n):
            print(" ", end = " ")
        for j in range(i+1):
            print("*", end = " ")
            if (j == 0): continue
            print("*", end = " ")
        print()
    for i in range(1,n):                 # if u want to do 1 less,(in decreasing-ROW) then include start condition (i.e. i, 1, ...)
    # for i in range(n-1):               # it exclude last row
        for j in range(i+1):             
            print(" ", end = " ")
        for j in range(i,n):
            print("*", end = " ")
            if (j == n-1): continue         
            print("*", end = " ")
        print()

def pyramid(n):
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end = "")
        for j in range(i+1):
            print("* ", end = "")       # its just right-increasing triangle with "* " (star + space)
        print()

def reverse_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end = "")
        for j in range(i,n):
            print("* ", end = "")
        print()

def double_pyramid(n):
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end = "")
        for j in range(i+1):
            print("* ", end = "")
        for j in range(i,n-1):
            # if (j == n-2): continue
            print("  ", end = "")
        for j in range(i+1):
            # if (j == n-1): continue
            print("* ", end = "")
        print()

def left_pascel_triangle(n):
    for i in range(n-1):
        for j in range(i+1):
            print("*", end = ' ')
        print()
    for i in range(n):
        for j in range(i,n):
            print("*", end = ' ')
        print()

def right_pascel_triangle(n):
    for i in range(n-1):
        for j in range(i,n-1):
            print(" ", end = " ")
        for j in range(i+1):
            print("*", end = " ")
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end = " ")
        for j in range(i,n):
            print("*", end = " ")
        print()
            
def butterfly(n):
    for i in range(n-1):
        for j in range(i+1):
            print("*", end = " ")
        for j in range(i,n-1):
            print(" ", end = " ")
            if (j == n-2): continue
            print(" ", end = " ")
        # for j in range(i,n-2):          # either we can level up triangle using i or remove 1 item each from it 
        #     print(" ", end = " ")
        for j in range(i+1):
            print("*", end = " ")
        print()
    for i in range(n):
        for j in range(i,n):
            print("*", end = " ")
        for j in range(i):
            print(" ", end = " ")         # total 2 hidden triangle so 3 + 1(end) = 4 space
        for j in range(i-1):
            print(" ", end = " ")
        for j in range(i,n):
            if (j == 0): continue         # for middle face
            print("*", end = " ")
        print()


def sandglass(n):
    for i in range(n-1):
        for j in range(i+1):
            print(" ", end = "")
        for j in range(i,n):
            print("* ", end = "")
        print()
    for i in range(n):
        for j in range(i,n):
            print(" ", end = "")
        for j in range(i+1):
            print("* ", end = "")
        print()

def hollow_square(n):
    for i in range(n):
        if (i == 0 or i == n-1):
            for j in range(n):
                print("*",end = " ")
        else:
            for j in range(n):
                if(j == 0 or j == n-1):
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
        print()

def hollow_triangle(n):
    for i in range(n):
        if (i == n-1):
            for j in range(n):
                print("*", end = " ")
            for j in range(n):
                if (j == 0): continue
                print("*", end = " ")
                # if (j == 0):
                #     print("*", end = " ")
        else:
            for j in range(i,n-1):
                print(" ", end = " ")
            for j in range(i+1):
                if(j == 0):
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            for j in range(i):
                if(j == i-1):
                # if ( j == 0): continue
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
        print()

num = 5
# square(num)
# increasiing_triangle(num)
# decreasing_triangle(num)
# right_increasing_triangle(num)
# right_decreasing_triangle(num)
# hill (num)
# reverse_hill(num)
# dimond(num)
# pyramid(num)
# reverse_pyramid(num)
# double_pyramid(num)
# left_pascel_triangle(num)
# right_pascel_triangle(num)
# butterfly(num)
# sandglass(num)
# hollow_square(num)
# hollow_triangle(num)

def increasiing_triangle1(n):
    a = 'A'
    for i in range(n):
        
        for j in range(i+1):
            print(a, end = " ")
            a = chr(1 + ord(a)) 
        print()

def pyramid1(n):
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end = "")
        for j in range(i+1):
            print(f"{ncr(i,j)} ", end = "")       # its just right-increasing triangle with "* " (star + space)
        print()    

def ncr(i,j):
    # try:
        return fact(i)//(fact(j)*fact(i-j))
    # except ValueError as e:
    #     print(f"error:{e}")
    #     return None

def fact(n):
    # if (n < 0): raise ValueError("negative")
    if (n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)
# increasiing_triangle1(num)
# pyramid1(num)

# print(ncr(3,4))

# grid = [[10 for _ in range(3)] for _ in range(5)]
# print(grid)

def ncr_pascal_triangle(n, r):
    if r < 0 or r > n:
        return 0

    # Initialize a 2D list (or array)
    pascal = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        pascal[i][0] = 1

    # Fill the table using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    print(pascal)
    return pascal[n][r]

# ncr_pascal_triangle(3,3)

def spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0,n-1,0,n-1
    val = 1

    while top<=bottom and left<= right:
        for i in range(left, right+1):
            matrix[top][i] = val
            val += 1
        top += 1

        for i in range(top, bottom+1):
            matrix[i][right] = val
            val += 1
        right -= 1

        for i in range(right, left-1,-1):
            matrix[bottom][i] = val
            val += 1
        bottom -= 1

        for i in range(bottom, top-1, -1):
            matrix[i][left] = val
            val += 1
        left += 1

    # print(matrix)
    for row in matrix:
        print(*row)

# spiral_matrix(3)

def wave_matrix(m,n):
    val = 1
    matrix = [[0]*n for _ in range(m)]
    col = 0
    while col < n:
        for i in range(m):
            matrix[i][col] = val
            val += 1
        col += 1
        if col != n:
            for i in range(m-1,-1,-1):
                matrix[i][col] = val
                val += 1
            col += 1
    for row in matrix:
        print(*row)
# wave_matrix(3,5)

def hollow_dimond(n):
    # for i in range(n-1):
    #     print(' '*(n-i-1) + "*"*(2*i+1))
    # for i in range(n,0,-1):
    #     print(" "*(n-i) + "*"*(2*(i-1)+1))
   
    for i in range(n):
  # for i in range(n-1):                # we can perform it to n-1 to omit last row, then we can use range(n) in 2nd loop
        for j in range(i,n):
            print(" ", end = " ")
        for j in range(i+1):
            if (j == 0):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        for j in range(i):
            if (j == i-1):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
    for i in range(1,n):                 # if u want to do 1 less,(in decreasing-ROW) then include start condition (i.e. i, 1, ...)
    # for i in range(n-1):               # it exclude last row
        for j in range(i+1):             
            print(" ", end = " ")
        for j in range(i,n-1):
            if (j == i):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        for j in range(i,n):
            if (j == n-1):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

# hollow_dimond(7)

# def longest_palindrome_substring(s):
#     rs = ""
#     for char in s:
#         rs = rs + char
#         if (rs == reverse(rs))
# left_pascel_triangle("ABABADC")


