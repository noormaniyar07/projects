n=int(input("enter the number:"))
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
print(l)