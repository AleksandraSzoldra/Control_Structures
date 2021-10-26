#ZAD_14

x=int(input("Enter number: "))

quantity=0
sum=x
mean=0

if x==0:
    print("Different from 0 please.")
else:
    while x!=0: 
        x=int(input("Enter number: "))
        quantity+=1
        sum+=x
    
    print(f"Quantity: {quantity}, Sum: {sum}, Mean: {sum/quantity}")
        
         
        
        
# mean+=x/(quantity)
    
    