x=int(input("Enter first number: ")) 
y=int(input("Enter second number: "))  
 
if x>y and x!=y:
    print(f"Numbers in ascending order: {x},{y}")
if y>x and x!=y:
    print(f"Numbers in ascending order: {y},{x}")
if x==y:
    print("You have to pick two different numbers!") 