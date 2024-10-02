s=input("enter the string:")
a="true"
for i in range(len(s)-1):
    if ((s[i]=="[" and s[i+1]=="]")or(s[i]=="{" and s[i+1]=="}")or(s[i]=="(" and s[i+1]==")" )):
        continue
    else:
        a="false"
        break
print(a)
        pending