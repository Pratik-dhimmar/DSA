def Smallest_positive_no(array):
    array.sort()
    print(array)
    unreachable =  1
    for x in array:
        if(x <= unreachable):
            unreachable += x
            # print(unreachable)
        else:
            break
    return unreachable


array = [1,2,5,3]
answer = Smallest_positive_no(array)
print(answer)