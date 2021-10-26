x=int(input("Enter the amount in PLN: ")) 

if x<0: 
    print ("Choose a positive number!!!")
if x%5==0:
    five=x//5
    print (f"5zł: {five}")
if x%5!=0:
    five=x//5
    two= (x-(five*5))//2
    one=(x-((five*5)+(two*2)))//1
    print(f"The amount of  PLN in coins: 5zł-{five}, 2zł-{two}, 1zł-{one}")
    