#ZAD_13
f1=0
f2=1
i=2
n=50 #numer wyrazu
while i<n:
    fib=f1+f2
    f1=f2
    f2=fib
    i+=1
    print(fib, end="  ")