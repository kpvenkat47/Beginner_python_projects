#Recursion
def fibr(a):
    """Find Fibonacci number of User input"""
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibr(a-1)+fibr(a-2)
try:
    user_input=int(input("Enter Number:"))
except:
    print("Enter number only")
else:
    print(f"Fibonacci number of {user_input} = {fibr(user_input)}")
    
    
    
#List    
def fibl(a):
    """Find Fibonacci number of User input"""
    f=[0,1]
    for i in range(2,a+1):
        f.append(f[i-1]+f[i-2]) #list_Possition_store_Fibonaccivalue
    return f[a]

try:
    n=int(input("Enter Number:"))
except:
    print("Enter number only")
else:
    print(f"Fibonacci number of {n} = {fibl(n)}")
    


