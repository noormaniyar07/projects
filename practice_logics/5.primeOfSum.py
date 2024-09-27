print("enter the number")
a=int(input())
n=0
count=0
s=0
while a > 0:
    r=a%10
    s=s+r
    a=a//10

for i in range(1,s+1):
    if s%i == 0:
        count = count + 1
        
if count==2:
    print(f"given number  is a prime number")
else:
    print("not a prime number")