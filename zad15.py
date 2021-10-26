#ZAD_15
n=int(input("Natural number: "))

i=1
x=2 #Każda liczba dzieli się przez jeden i samą siebie
y=0 #Dzielniki poza x

if n>=1:
    while i<=n:
        if n%i==0 and i==n: #Podzielne przez samą siebie     
           x+=1
        if n%i==0 and i!=n and i!=1: #Podzielne przez cokolwiek rozne od n 
            y+=1
        
        i+=1
    if x!=2 and y==0:
        print (f"Liczba {n} jest liczbą pierwszą.")
    else:
        print (f"Liczba {n} nie jest liczbą pierwszą.")
        