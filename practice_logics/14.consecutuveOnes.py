list=[4,1,1,3,1,1,1,1,3,1,1,3]
max=0
count=0
for i in list:
    if i==1:
        count+=1
        if (count>=max):
            max=count
    else:
        
        count=0
        
print(max)