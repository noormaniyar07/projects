l=int(input("plese enter len of list"))
list=[]
for i in range(l):
    a=int(input(f"enter {i}th element"))
    list.append(a)

for i in range(l-1):
    for j in range(l-1-i):
        if list[j] > list[j+1]:
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
       
print(list)