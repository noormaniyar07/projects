# for int value reversing
# a=456
# n=0
# while a > 0:
#     r=a%10
#     n=r+n*10
#     a=a//10
    
# print(n)

print("enter the number")
a=int(input())
n=0
count=0
s=0
while a > 0:
    r=a%10
    s=s+r
    a=a//10

for i in range(1,s+1):
    if s%i == 0:
        count = count + 1
        
if count==2:
    print(f"given number  
          is a prime number")
else:
    print("not a prime number")
    
    
# # Input the number
# print("Enter the number")
# a = int(input())

# # Initialize sum to 0
# s = 0

# # Calculate the sum of the digits of the number
# while a > 0:
#     r = a % 10  # Get the last digit
#     s = s + r   # Add the digit to the sum
#     a = a // 10 # Remove the last digit

# # Check if the sum is a prime number
# count = 0
# for i in range(1, s + 1):
#     if s % i == 0:
#         count += 1

# # If the sum has exactly two divisors, it's prime
# if count == 2:
#     print(f"The sum of the digits is {s}, which is a prime number.")
# else:
#     print(f"The sum of the digits is {s}, which is not a prime number.")