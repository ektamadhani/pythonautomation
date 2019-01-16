class Emp:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
        #print(self.eid)
        #print(self.ename)
    def m1(self):
        self.sal=1000
        #print(self.sal)
e1=Emp(1,'A')
e1.m1()
del e1.eid
print(e1.__dict__)
print('----------')
e2=Emp(2,'B')
e2.m1()
print(e2.__dict__)


              
        
