l1=[4,3,6,7,4]
l2=[3,1,9,0,2]
s=sorted(l1+l2)
print(s)
l=len(s)
if l%2==0:
    m=(s[l//2]+s[l//2-1])/2
    print(m)
else:
    print(s[l//2])
    