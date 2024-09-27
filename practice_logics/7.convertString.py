string=input("enter the string")
rstring=string[::-1].split()
for word in rstring:
    print(len(word) , word)