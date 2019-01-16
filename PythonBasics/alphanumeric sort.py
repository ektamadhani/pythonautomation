s=input("enter an alphanumeric value")
s1=s2=finalval=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    finalval=finalval+x
for x in sorted (s2):
    finalval=finalval+x
print(finalval)
    
    
