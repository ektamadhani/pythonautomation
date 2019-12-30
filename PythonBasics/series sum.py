##n = int(input("Enter a num: "))
##if n <0:
##    print ("Enter a Positive Number")
##else:
##    num=0
##    for i in range(1,n+1):
##        ans = num +i
##        print ans,end = "+"
##    sum = n*(n+1)/2
##    print "The sum is", sum

n=int(input("Enter a number: "))
a=[]
for i in range(1,n+1):
    print(i,sep = " ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
    print("=",sum(a))
    print()

    
