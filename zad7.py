for i in range (1,31): 
    if i%3==0:
        if i%5==0:
            print(f"{i} BINGO")
        else:
            print (f"{i} THREE")
    if i%5==0 and i%3!=0: 
        print (f"{i} FIVE")   
    if i%3!=0 and i%5!=0: 
        print (i) 
    i+=1 
