class my_class():
    def abc(self):
        a = str(12345)
        print "value of a" ,a 
    def xyz(self,arg1,arg2):
        sum = arg1 + arg2
        print "value of sum %s" %(sum)
        

class child_my_class(my_class):
    def abc(self):
        my_class.abc(self)
        print "pratik"
        
        
#Notice that when we call the method1 or method2, we don't have to supply the self-keyword. 
#That's automatically handled for us by the Python runtime.
#Python runtime will pass "self" value when you call an instance method on in instance, whether you provide it deliberately or not
#You just have to care about the non-self arguments 
 
        
def main():    
    # Calling method from base class
    o = my_class()
    o.abc()
    o.xyz(5,9)
    
    # calling method for derived class
    #Notice that the in childClass, xyz is not defined but it is derived from the parent myClass.
    z = child_my_class()
    z.abc()
    z.xyz(8,8)


if __name__== "__main__":
  main()
         
#The self-argument refers to the object itself. 
#Hence the use of the word self. So inside this method, self will refer to the specific instance of this object that's being operated on.
#Self is the name preferred by convention by Pythons to indicate the first parameter of instance methods in Python. 
#It is part of the Python syntax to access members of objects         