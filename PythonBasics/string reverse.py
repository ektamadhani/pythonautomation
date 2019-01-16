s=input("Enter a string value")
i=len(s)-1
finalstr=''
while i>=0:
    finalstr=finalstr+s[i]
    i=i-1
print(finalstr)

#slicing
s="python"
print(s[: : -1])

#to print s="qspiders"
#q=0
#s=1
#p=2
#i=3
#d=4
#e=5
#r=6
#s=7
#method1
s="qspiders"
for i in range(0,len(s),2):
    print(i,s[i])
for j in range(1,len(s),2):
    print(j,s[j])


#method2
s=input("enter string value")
i=0
print("Even position chare")
while i<len(s):
    print(i,'',s[i])
    i=i+2
print("")
print("odd Position chars")
i=1
while i<len(s):
    print(i,'',s[i])
    i=i+2
    
    

