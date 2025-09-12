def move_0_toLast(no):
    i = str(no).count('0')
    # l = []
    for x in str(no):
        if x == '0' : continue
        print(x,end='')
        # l.append(x)
    print('0'*i)
    # l.append('0'*i)
    # return "".join(l)

(move_0_toLast(1202130033))