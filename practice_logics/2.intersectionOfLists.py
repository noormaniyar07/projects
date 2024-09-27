l1=[3,5,6,8]
l2=[5,8,4,7]
inters=[]
for i in l1:
    if i not in l2:
        inters.append(i)
        
print(inters)
        