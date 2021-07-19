user_word=input("Enter a Word:")
print(f"Your value=",user_word)
palindrome=user_word[len(user_word)-1::-1]
if(user_word==palindrome):
    print("It is palindrome")
else:
    print("nope,it is not a palindrome")
