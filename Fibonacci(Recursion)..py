def fibo(a):
    f=[0,1]
    for i in range(2,a+1):
        f.append(f[i-1]+f[i-2])
    return f[a]

try:
    n=int(input("Enter Number:"))
except:
    print("Enter number only")
else:
    print(f"Fibonacci number of {n} = {fibo(n)}")



