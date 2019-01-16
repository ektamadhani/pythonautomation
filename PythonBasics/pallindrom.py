s="madam"
finalstr=s[: : -1]
if s==finalstr:
    print(s,"is a pallindrom")
else:
    print(s,"is Not a pallindrom")


s=input("Enter a string value")
i=len(s)-1
finalstr=''
while i>=0:
    finalstr=finalstr+s[i]
    i=i-1
if s==finalstr:
    print(s,"is a pallindrom")
else:
    print(s,"is Not a pallindrom")




