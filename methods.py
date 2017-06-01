class pizza():
    pratik = 1
    def __init__(self):
        print "hello"
    def get_size1(self):
        return "123"


class dabali(pizza):
    def get_size(self,pratik):
        self.pratik = pizza.pratik
        print self.pratik
        return 123


z = dabali()
z.get_size(5)