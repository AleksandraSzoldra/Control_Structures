x=int(input("Enter the first coordinate: ")) 
y=int(input("Enter the second coordinate: "))  

if x>0 and y>0: 
    print (f"Point P({x},{y}) is located in the first quadrant")
if x<0 and y>0: 
        print (f"Point P({x},{y}) is located in the second quadrant")
if x<0 and y<0: 
        print (f"Point P({x},{y}) is located in the third quadrant")
if x>0 and y<0: 
        print (f"Point P({x},{y}) is located in the fourth quadrant") 
if x==0 and y==0: 
        print (f"Point P({x},{y}) is located in the middle of coordinate system")


