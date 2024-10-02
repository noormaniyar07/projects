l=[2,4,3,7,5,1,-3,-5,4,6,8]
r=[]
for i in range(len(l)-2):
    if l[i]>l[i+1]:
        if l[i]>l[i+2]:
            r.append(l[i])
        else:
            r.append(l[i+2])
    elif l[i+1]>l[i+2]:
        r.append(l[i+1])
    else:
        r.append(l[i+2])
print(r)