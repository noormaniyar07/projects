# s=input('enter the string')
# rs=s[::-1]
# rsl=rs.split()
# print(rsl)
n=int(input("enter number of letters in string"))
s=[]
print("enter elements")
for i in range(n):
    a=input()
    s.append(a)
print(s[::-1])