print "How to declare and use a variable"
a=100
print a;


#You can re-declare the variable even after you have declared it once.
#Here we have variable initialized to f=0.
#Later, we re-assign the variable f to value "pratik"
print "How to re-declare variables "
f=0
print 'value after first declaration :',f ;

f="Pratik"
print 'value after second declaration :', f ;


print "Concatenate Variables"
a=10
b="Pratik"
print "Concate answer of a and b is : ", str(a) + b;


print "Local and Global variable"
print "Value of global variable :",a;

def abc():
    global a
    print a;
    a = "My Name is Pratik"
    print "Value of local variable:",a;

abc()
print "Value of global variables :",a;




print "Delete Variable"
x=100
print x;
del x
print x;


    
