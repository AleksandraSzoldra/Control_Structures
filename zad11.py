pin="0805"
pin_code=str(input("Enter the pin code: "))

if pin_code!=pin:
    print ("Incorrect PIN.")
    for i in range (1,3): 
        pin_code=str(input("Enter the pin code: "))
        if pin_code!=pin:
            print("Incorrect PIN.")
    print("Sorry, your payment card has been blocked.")

else:
    print("PIN is correct.")
        
    
    