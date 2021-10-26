a=int(input("Width: "))
b=int(input("Lenght: "))

print (a*"*")
for i in range (1,b-1):
    print(("*"+(" "*(a-2))+"*"))
    
print(a*"*")
