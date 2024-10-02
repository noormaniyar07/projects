l=[2,4,0,6,4,0,0,4,0,4,0,4,0]
r=[]
c=0
for i in l:
    if i==0:
        c=c+1
    else:
        r.append(i)
for j in range(c):
    r.append(0)
print(r)

# l = [2, 4, 0, 6, 4, 0, 0, 4, 0, 4, 0, 4, 0]
# r = []
# c = 0

# for i in l:
#     if i == 0:
#         c = c + 1  # Count the zeroes
#     else:
#         r.append(i)  # Append non-zero elements to r

# # Add 'c' number of zeroes at the end of 'r'
# for j in range(c):
#     r.append(0)

# print(r)
