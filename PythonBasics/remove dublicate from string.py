s=input("Enter string val:")
l=[]
for x in s:
    if x  not in l:
        l.append(x)
        
finalval=''.join(l)
print(finalval)
