nterms=int(input("How many terms?"))
#first two terms
n1=0
n2=1
count=0
#check the number of terms is valid or not
if nterms<=0:
    print("please enter a positive number")
elif nterms==1:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibanacci series upto",nterms,":")
    while count<nterms:
        print(n1,end=',')
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
