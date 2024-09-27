num=int(input("enter the number"))
rn=0
while num > 0:
    r=num%10
    rn=rn*10+r
    num=num//10
print(rn)