a=int(input("Enter the number: "))
b=bin(a)
print(b)
l=list(b)
m=l[2:]

rs="".join(m[::-1])
rb='0b'+rs
print(rb)
print(eval(rb))
                
