def t(x):
    for i in range (1,8):
        print (x, end=" ")
        x+=7
    return True 

for i in range (1,8):
    t(i)
    print () 