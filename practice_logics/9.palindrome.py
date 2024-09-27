pal=input("please enter the string to check it is pal or not")
p=pal[::-1]
if pal == p:
    print(f"given string {pal} is a palindrome")
else:
    print(f"given string {pal} is not a palindrome")