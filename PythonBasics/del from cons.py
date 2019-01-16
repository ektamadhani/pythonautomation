class Emp:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
        #del self.ename
        print(self.eid)
        print(self.ename)
    def dispInfo(self):
        self.sal=100
        #del self.sal
        print(self.sal)
e1=Emp(1,'A')
e1.dispInfo()
del e1.ename
print(e1.ename)
