a=input("enter string")
b=input("enter string")
a=sorted(a)
b=sorted(b)
if a==b:
    print(f"given strings are anagrams")
else:
    print("given strings are not anagrams")