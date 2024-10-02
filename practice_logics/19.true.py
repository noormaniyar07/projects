l=[4,3,2,1,1,3,5,1,1,1]
c=0
a="false"
for i in (l):
    if i==1:
        c=c+1
        if c>=3:
            a="true"
            break
    else:
        c=0
print(a)