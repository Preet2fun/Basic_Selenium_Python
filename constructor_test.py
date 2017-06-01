class MyClassCustom():
    def __init__(self,exp,salary):
        self.exp = exp
        self.salary = salary
    def __init__(self,fname,lname,add):
        self.fname = fname
        self.lname = lname
        self.add = add

y = MyClassCustom(5,10000)
z = MyClassCustom('a','b','c')
print y.exp
print y.salary