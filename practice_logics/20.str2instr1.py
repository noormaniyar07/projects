s1=input("enter the string")
s2=input("enter the string")
s3=" "
for i in (s1):
    if i not in s2:
        s3=s3+i
print(s3)