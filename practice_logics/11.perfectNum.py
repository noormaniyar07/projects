n=int(input("enter number"))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+i

if n==count:
    print(f"given number {n} is a perfect number")
else:
    print(f"given number {n} is not a perfect number")