a=int(input("enter a number"))
count=0
s=0
for i in range(1,a+1):
    for j in range(2,i):
        if i%j==0:
            count=count+1
    if count==1:
        s=i+s
print(s)
    pending