#Any arguments or input parameters should be placed within these parentheses
#The function first statement can be an optional statement- docstring or the documentation string of the function
#The code within every function starts with a colon (:) and should be indented (space)
#The statement return (expression) exits a function, optionally passing back a value to the caller. 
#A return statement with no arguments is the same as return None.


def abc():
    print "My Name is Pratik"
    print "I Love football"
    return 100

# Case 1
def xyz(a):
    print a*a;
    
# Case 2
def aaa(a):
    b=a*a;
    
# Case 3
def bbb(a):
    return a*a    

# Case 4
def ccc(a):
    return a*a 


abc()
print abc()

print "Output of first case"
print xyz(4)
#This is because when you call the function, recursion does not happen 
#and fall off the end of the function. Python returns "None" for failing off the end of the function.



print "Output of second case"
print aaa(4)
#When you run the command "print aaa (4)" it actually returns the value of the object since 
#we don't have any specific function to run over here it returns "None".


print "Output of third case"
print bbb(4)
#When you use the "return" function and execute the code, it will give the output "16."


print "Output of forth case"
print ccc
#Functions in Python are themselves an object, and an object has some value. We will here see how Python treats an object. 
#When you run the command "print square" it returns the value of the object. Since we have not passed any argument, 
#we don't have any specific function to run over here it returns a default value for example (0x021B2D30) which is the location of the object


#Function calling with argument
# type 1

def arg_plus(x,y):
    print x + y;
    
arg_plus(5,5)    

# type 2
def arg_multy(x,y=0):
    print x * y;
    
arg_multy(5) 

# type 3
#This time we will change the value to y=3 instead of the default value y=0, and it will return the output as (5-3)=2.
def arg_sub(x,y=0):
    print x - y;
    
arg_sub(5,y=3) 

# type 4
#no matter what the argument is passed, but its value preserved.
def arg_exchange(x,y=0):
    print "value of x", x;
    print "value of y", y;
    
arg_exchange(y=5,x=3) 
    
# type 5
#Multiple Arguments can also be passed as an array. Here in the example we call the multiple arguments (1,2,3,4,5) 
#by calling the (*args) function.
def arg_exchange(*arg):
    print arg;
    

arg_exchange(1,2,3,4)      
