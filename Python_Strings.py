#Accessing Values in Strings

var1="pratik"
var2="zalak"
var3=100
print var1[2];
print var2[2:4];
print 't' in var1;
print 'y' in var1;
print 'y' not in var2;
print '%s %d' %(var1,var3);


a='pratik'
b='zalak'
print a+b;
print a*2;

x='Hello Word'
print x[:6];
print x[1:6];

#Python String replace() Method

old='I like Fotball'
new = old.replace('like','love')
print(new);

#Changing upper and lower case strings
w='i love telecome'
y='I LIKE SPORT'
print w.upper();
print y.lower();


#Using "join" function for the string
print ':'.join('Pratik');
print '+'.join(a);


#Reversing String
s='Cricket'
print ''.join(reversed(s));


#Split Strings
v='zalak pratik patel'
print v.split(' ');
print v.split('+');


#In Python, Strings are immutable.
a='pratik'
a.replace('pratik','zalak')
print a;

b='football'
b=b.replace('football','cricket')
print b;
