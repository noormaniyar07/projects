s=int(input("enter the starting number"))
e=int(input("enter the ending mumber"))
sum=0
for i in range(s,e+1):
    sum+=i*i*i
print(sum)