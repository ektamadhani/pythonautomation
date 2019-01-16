class Test:
    count=0
    
    
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def m1(cls):
        print("Total obj.",Test.count)
t1=Test()
t2=Test()
t3=Test()
#t4=Test()
Test.m1()
t4=Test()
