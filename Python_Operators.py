# Assignment Operators

x = 3
y = 4
y+=x  # y = y + x 
print y;
x+=y  # x = x + y
print x 
x*=y  # x = x * y
print x 
x/=y  # x = x / y
print x 


# Membership operators

a=2
b=4
list = [1,2,3]
if a in list:
    print '%d'   'is in list' %(a); 
else:
    print  '%d'   'is not in list' %(a);

if b not in list:
    print '%d'   'is in list' %(b); 
else:
    print  '%d'  'is not in list' %(b);
