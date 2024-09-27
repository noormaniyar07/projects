s="11011101111011111101111"
count=0
for i in s:
    if i=='1':
        count=count+1
    else:
            print(chr(64+count),end="")
            count=0