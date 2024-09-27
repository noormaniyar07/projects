print("enter the number of elements in this list")
n=int(input())
list=[]
print(f"enter the {n} elements")
for j in range(n):
    e=int(input())
    list.append(e)
max=0
for i in list:
    if i>max:
        max=i
        

print("the max element in this list is :" ,max)