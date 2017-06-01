import re

#Example of w+ and ^ Expression
#"^": This expression matches the start of a string
#"w+": This expression matches the alphanumeric character in the string
x = "411prit 657yry, football is awsome, rsome1"
#r1=[];
r1 = re.findall(r"^\w+",x)
r2 = re.findall(r"^\w",x)
print r1
#print r1[1]
print r2


#Example of \s expression in re.split function
print (re.split(r'\s','we are splitting the words'))
print (re.split(r's','split the words'))

#Finding Pattern in Text (re.search())
abc = ['is','name','zalak']
xyz = "My name is pratik"
for a in abc:
    print "string '%s' is in %s -->" %(a,xyz)
    
    if re.search(a,xyz):
        print "match found"
    else:
        print "matc not found"
        
        
#Using re.match()
#The match function is used to match the RE pattern to string with optional flags. In this method, the expression "w+" and "\W" will match the words starting with letter 'g' and thereafter, 
#anything which is not started with 'g' is not identified. To check match for each element in the list or string, we run the forloop.

list = ["guru99 get", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
    
    if z:
        print(z.groups())
        
        
        
        
#Using re.findall for text
#Re.findall() module is used when you want to iterate over the lines of the file, it will return a list of all the matches 
#in a single step. For example, here we have a list of e-mail addresses, and we want all the e-mail addresses to be fetched out from the list,
# we use the re.findall method. It will find all the e-mail addresses from the list.        

abc='guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc) 
for email in emails:
    print email        
      