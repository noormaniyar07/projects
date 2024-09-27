
fact=(int(input("enter the num :")))
f=1
if fact>=0:
    if fact==0 | fact==1:
        print(f"factorial of {fact} is 1 ")
    else:
        for (i) in range(1,fact+1):
            f=f*i
            
        print(f"factorial of {fact} is {f}")
else:
    print("plese enter the valid positive number")