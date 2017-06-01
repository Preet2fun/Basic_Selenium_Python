#Basic example of Tuples

var=('jan','feb','march');
var1=('praik',99);
var2=(50,);
print var[0];
print var1[1];
print var2[0];
print var[0:3];


#Packing and Unpacking
#In packing, we place value into a new tuple while in unpacking we extract those values back into variables.

x=('PRATIK','PATEL',29);    # Packing
(first,last,Age)=x          # unpacking
print first;
print last;
print Age;

#Comparing tuples
a=(5,5);
b=(5,6);
if (a>b):
    print "a is grater then b"
else:
    print "b is grater then a"

#Tuples and dictionary
w = {'x':100,'y':200}
z = w.items()
print z;

#Deleting Tuple
a=(4,5,6);
del a;
#print a[0:3];


#Built-in functions with Tuple
p=('pratik',1,2,3);
z = max(p)
print 'maximum value from tuple is :',z;
y = min(p)
print 'minimum value from tuple is :',y;
h = sorted(p)
print h;
g = len(p[0])
print g;
