list=[1,3,5,7,9,8,7,5,3,1,4,6]
u=[]
for i in list:
    if i not in u:
        u.append(i)

print(u)