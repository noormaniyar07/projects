list=[4,0,2,4,7,0,5,0,6,7,4,0,5,6]
s=0
slist=[]
l=len(list)
for i in range(l):
    if list[i]!=0:
        s=list[i]+s
    else:
        slist.append(s)
        s=0
if s!=0:
    slist.append(s)
print(slist)
        