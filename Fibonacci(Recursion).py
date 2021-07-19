def fibor(a):
    """Find Fibonacci number of User input"""
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibor(a-1)+fibor(a-2)
try:
    user_input=int(input("Enter Number:"))
except:
    print("Enter number only")
else:
    print(f"Fibonacci number of {user_input} = {fibor(user_input)}")

