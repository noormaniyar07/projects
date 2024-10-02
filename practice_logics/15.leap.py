y=int(input("enter the year:"))
if y%4==0 & y%100!=0 | y%400 :
    print(f"gien year{y} is leap year")
else:
    print(f"given year {y} is not a leap year")